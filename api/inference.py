"""Synchronous single-image inference endpoint."""

from __future__ import annotations

from fastapi import APIRouter

from api import job_manager
from api.schemas import InferenceRequest, InferenceResponse

router = APIRouter(prefix="/v1/inference", tags=["inference"])


@router.post("/detect", response_model=InferenceResponse)
async def detect(req: InferenceRequest):
    """Block until Ray inference finishes and return detections inline."""
    result = job_manager.run_sync_inference(
        image_path=req.image_path,
        confidence_threshold=req.confidence_threshold,
        device=req.device,
    )
    return InferenceResponse(
        image_path=result["image_path"],
        car_count=result["car_count"],
        detections=result.get("detections", []),
        processing_time_ms=result["processing_time_ms"],
        worker_id=result["worker_id"],
        model=result["model"],
    )
