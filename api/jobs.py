"""Job routes — submit, status, result."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from api import job_manager
from api.schemas import (
    JobResultResponse,
    JobStatus,
    JobStatusResponse,
    JobSubmitRequest,
    JobSubmitResponse,
)

router = APIRouter(prefix="/v1/jobs", tags=["jobs"])


@router.post("/submit", response_model=JobSubmitResponse, status_code=202)
async def submit_job(req: JobSubmitRequest):
    """Accept a JobSubmitRequest, dispatch to Ray, return job_id immediately."""
    job = job_manager.submit_job(req)
    return JobSubmitResponse(
        job_id=job["job_id"],
        status=job["status"],
        submitted_at=job["submitted_at"],
        num_images=job["num_images"],
    )


@router.get("/{job_id}/status", response_model=JobStatusResponse)
async def get_job_status(job_id: str):
    job = job_manager.get_job(job_id)
    if not job:
        raise HTTPException(404, detail="Job not found")
    return JobStatusResponse(
        job_id=job["job_id"],
        status=job["status"],
        submitted_at=job["submitted_at"],
        started_at=job.get("started_at"),
        completed_at=job.get("completed_at"),
        progress=job.get("progress"),
        error=job.get("error"),
    )


@router.get("/{job_id}/result", response_model=JobResultResponse)
async def get_job_result(job_id: str):
    job = job_manager.get_job(job_id)
    if not job:
        raise HTTPException(404, detail="Job not found")
    if job["status"] in (JobStatus.queued, JobStatus.running):
        raise HTTPException(409, detail=f"Job still {job['status'].value}")
    if job["status"] == JobStatus.failed:
        raise HTTPException(500, detail=job.get("error", "Unknown error"))

    elapsed = None
    if job.get("completed_at") and job.get("started_at"):
        elapsed = (job["completed_at"] - job["started_at"]).total_seconds()

    return JobResultResponse(
        job_id=job["job_id"],
        status=job["status"],
        results=job.get("results", []),
        summary=job.get("summary", {}),
        elapsed_seconds=elapsed,
    )
