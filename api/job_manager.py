"""In-memory job store, Ray dispatch, background monitor loop, WebSocket broadcast."""

from __future__ import annotations

import asyncio
import logging
import time
import uuid
from datetime import datetime, timezone
from typing import Any

import ray

from api.schemas import JobStatus, JobSubmitRequest, WSEvent

logger = logging.getLogger("api.job_manager")

# ── In-memory store ──────────────────────────────────────────────────────────

_jobs: dict[str, dict[str, Any]] = {}
_job_futures: dict[str, list[ray.ObjectRef]] = {}
_ws_clients: set[asyncio.Queue] = set()
_monitor_task: asyncio.Task | None = None


def _now() -> datetime:
    return datetime.now(timezone.utc)


# ── CarDetectionWorker (Ray remote actor) ────────────────────────────────────
# Mirrors the actor defined in the notebook so that the API can spawn its own
# workers without requiring the notebook to be running.

@ray.remote
class CarDetectionWorker:
    """Detects cars in images using torchvision Faster R-CNN on Ray cluster nodes."""

    def __init__(self, device: str = "cpu"):
        import uuid as _uuid

        import torch
        import torchvision

        self.worker_id = str(_uuid.uuid4())
        self.device = device if torch.cuda.is_available() or device == "cpu" else "cpu"
        self.model_name = "fasterrcnn_resnet50_fpn"
        self.processed_count = 0
        self.total_processing_time = 0.0

        self.model = torchvision.models.detection.fasterrcnn_resnet50_fpn(
            weights=torchvision.models.detection.FasterRCNN_ResNet50_FPN_Weights.DEFAULT,
        )
        self.model.to(self.device)
        self.model.eval()

        self.vehicle_classes = {3: "car", 6: "bus", 8: "truck"}
        self.transform = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
        ])

    def detect_from_bytes(self, image_bytes: bytes, image_name: str,
                          confidence_threshold: float = 0.5) -> dict:
        import os
        import tempfile
        import time as _time

        import torch
        from PIL import Image as PILImage

        suffix = "." + image_name.rsplit(".", 1)[-1]
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as f:
            f.write(image_bytes)
            tmp_path = f.name

        start = _time.time()
        try:
            img = PILImage.open(tmp_path).convert("RGB")
            img_tensor = self.transform(img).unsqueeze(0).to(self.device)

            with torch.no_grad():
                predictions = self.model(img_tensor)[0]

            car_count = 0
            detections: list[dict] = []
            for label, score, box in zip(
                predictions["labels"].cpu().tolist(),
                predictions["scores"].cpu().tolist(),
                predictions["boxes"].cpu().tolist(),
            ):
                if label in self.vehicle_classes and score >= confidence_threshold:
                    car_count += 1
                    detections.append({
                        "class": self.vehicle_classes[label],
                        "confidence": round(score, 3),
                        "bbox": [round(c, 1) for c in box],
                    })

            elapsed_ms = (_time.time() - start) * 1000
            self.processed_count += 1
            self.total_processing_time += elapsed_ms

            return {
                "status": "success",
                "image_path": image_name,
                "car_count": car_count,
                "detections": detections,
                "processing_time_ms": round(elapsed_ms, 2),
                "worker_id": self.worker_id,
                "model": self.model_name,
            }
        except Exception as e:
            return {
                "status": "error",
                "image_path": image_name,
                "car_count": 0,
                "error": str(e),
                "processing_time_ms": round((_time.time() - start) * 1000, 2),
                "worker_id": self.worker_id,
                "model": self.model_name,
            }
        finally:
            os.unlink(tmp_path)

    def get_stats(self) -> dict:
        avg = (self.total_processing_time / self.processed_count
               if self.processed_count else 0)
        return {
            "worker_id": self.worker_id,
            "processed_count": self.processed_count,
            "avg_processing_time_ms": round(avg, 2),
            "model_name": self.model_name,
            "device": self.device,
        }


# ── Public helpers ────────────────────────────────────────────────────────────

def get_job(job_id: str) -> dict[str, Any] | None:
    return _jobs.get(job_id)


def queue_depth() -> int:
    return sum(
        1 for j in _jobs.values() if j["status"] in (JobStatus.queued, JobStatus.running)
    )


def submit_job(req: JobSubmitRequest) -> dict[str, Any]:
    """Create a job record, dispatch work to Ray, and return immediately."""
    from pathlib import Path

    job_id = str(uuid.uuid4())
    now = _now()

    job: dict[str, Any] = {
        "job_id": job_id,
        "status": JobStatus.queued,
        "submitted_at": now,
        "started_at": None,
        "completed_at": None,
        "num_images": len(req.image_paths),
        "progress": None,
        "error": None,
        "results": [],
    }
    _jobs[job_id] = job

    # Spawn workers and submit tasks
    workers = [
        CarDetectionWorker.remote(device=req.device)
        for _ in range(req.num_workers)
    ]

    futures: list[ray.ObjectRef] = []
    for idx, img_path in enumerate(req.image_paths):
        worker = workers[idx % len(workers)]
        image_bytes = Path(img_path).read_bytes()
        image_name = Path(img_path).name
        ref = ray.put(image_bytes)
        futures.append(
            worker.detect_from_bytes.remote(ref, image_name, req.confidence_threshold)
        )

    job["status"] = JobStatus.running
    job["started_at"] = _now()
    _job_futures[job_id] = futures

    # Broadcast submission event
    _broadcast(WSEvent(event="job_submitted", job_id=job_id, data={"num_images": len(req.image_paths)}))

    return job


def run_sync_inference(image_path: str, confidence_threshold: float = 0.5,
                       device: str = "cpu") -> dict[str, Any]:
    """Block until a single image is processed and return the result."""
    from pathlib import Path

    worker = CarDetectionWorker.remote(device=device)
    p = Path(image_path)
    image_bytes = p.read_bytes()
    ref = ray.put(image_bytes)
    result = ray.get(worker.detect_from_bytes.remote(ref, p.name, confidence_threshold))
    return result


# ── WebSocket ────────────────────────────────────────────────────────────────

def register_ws(queue: asyncio.Queue) -> None:
    _ws_clients.add(queue)


def unregister_ws(queue: asyncio.Queue) -> None:
    _ws_clients.discard(queue)


def _broadcast(event: WSEvent) -> None:
    payload = event.model_dump_json()
    for q in list(_ws_clients):
        try:
            q.put_nowait(payload)
        except asyncio.QueueFull:
            pass


# ── Background monitor ───────────────────────────────────────────────────────

async def _monitor_loop(interval: float = 1.0) -> None:
    """Poll running jobs and finalise them when all Ray futures are ready."""
    while True:
        for job_id, futures in list(_job_futures.items()):
            job = _jobs[job_id]
            if job["status"] not in (JobStatus.running, JobStatus.queued):
                continue

            ready, remaining = ray.wait(futures, num_returns=len(futures), timeout=0)

            job["progress"] = f"{len(ready)} / {len(futures)}"

            if not remaining:
                try:
                    results = ray.get(ready)
                    job["results"] = results
                    job["status"] = JobStatus.completed
                    job["completed_at"] = _now()

                    successful = [r for r in results if r.get("status") == "success"]
                    total_cars = sum(r.get("car_count", 0) for r in successful)
                    job["summary"] = {
                        "total_images": len(results),
                        "successful": len(successful),
                        "failed": len(results) - len(successful),
                        "total_cars": total_cars,
                    }
                    _broadcast(WSEvent(
                        event="job_completed", job_id=job_id,
                        data={"summary": job["summary"]},
                    ))
                except Exception as exc:
                    job["status"] = JobStatus.failed
                    job["completed_at"] = _now()
                    job["error"] = str(exc)
                    _broadcast(WSEvent(
                        event="job_failed", job_id=job_id,
                        data={"error": str(exc)},
                    ))
                finally:
                    _job_futures.pop(job_id, None)

        await asyncio.sleep(interval)


def start_monitor() -> None:
    global _monitor_task
    if _monitor_task is None or _monitor_task.done():
        loop = asyncio.get_event_loop()
        _monitor_task = loop.create_task(_monitor_loop())
        logger.info("Job monitor started")


def stop_monitor() -> None:
    global _monitor_task
    if _monitor_task and not _monitor_task.done():
        _monitor_task.cancel()
        _monitor_task = None
        logger.info("Job monitor stopped")
