"""Bidirectional WebSocket for real-time job events."""

from __future__ import annotations

import asyncio
import json
import logging

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from api import job_manager
from api.schemas import JobSubmitRequest

logger = logging.getLogger("api.stream")

router = APIRouter(tags=["stream"])


@router.websocket("/v1/stream")
async def stream(ws: WebSocket):
    """
    Clients receive job_submitted / job_completed / job_failed events.

    Clients can also submit jobs by sending:
        {"action": "submit", "payload": { <JobSubmitRequest fields> }}
    """
    await ws.accept()

    queue: asyncio.Queue = asyncio.Queue(maxsize=256)
    job_manager.register_ws(queue)

    async def _sender():
        try:
            while True:
                msg = await queue.get()
                await ws.send_text(msg)
        except asyncio.CancelledError:
            pass

    sender_task = asyncio.create_task(_sender())

    try:
        while True:
            raw = await ws.receive_text()
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                await ws.send_text(json.dumps({"error": "invalid JSON"}))
                continue

            action = data.get("action")
            if action == "submit":
                try:
                    req = JobSubmitRequest(**data.get("payload", {}))
                    job = job_manager.submit_job(req)
                    await ws.send_text(json.dumps({
                        "event": "job_submitted",
                        "job_id": job["job_id"],
                        "num_images": job["num_images"],
                    }))
                except Exception as exc:
                    await ws.send_text(json.dumps({
                        "event": "error",
                        "detail": str(exc),
                    }))
            else:
                await ws.send_text(json.dumps({"error": f"unknown action: {action}"}))

    except WebSocketDisconnect:
        logger.info("WebSocket client disconnected")
    finally:
        sender_task.cancel()
        job_manager.unregister_ws(queue)
