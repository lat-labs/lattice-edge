"""Pydantic models for all request / response payloads."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ── Job lifecycle ────────────────────────────────────────────────────────────

class JobStatus(str, Enum):
    queued = "queued"
    running = "running"
    completed = "completed"
    failed = "failed"


class JobSubmitRequest(BaseModel):
    """POST /v1/jobs/submit"""
    image_paths: list[str] = Field(
        ..., min_length=1,
        description="Paths to images *inside* the container (e.g. /home/latlab/work/notebooks/images/photo.jpg).",
    )
    confidence_threshold: float = Field(0.5, ge=0.0, le=1.0)
    num_workers: int = Field(3, ge=1, le=32)
    device: str = Field("cpu", description="'cpu' or 'cuda'")


class JobSubmitResponse(BaseModel):
    job_id: str
    status: JobStatus = JobStatus.queued
    submitted_at: datetime
    num_images: int


class JobStatusResponse(BaseModel):
    job_id: str
    status: JobStatus
    submitted_at: datetime
    started_at: datetime | None = None
    completed_at: datetime | None = None
    progress: str | None = None  # e.g. "7 / 12"
    error: str | None = None


class JobResultResponse(BaseModel):
    job_id: str
    status: JobStatus
    results: list[dict[str, Any]] = []
    summary: dict[str, Any] = {}
    elapsed_seconds: float | None = None


# ── Inference (synchronous) ──────────────────────────────────────────────────

class InferenceRequest(BaseModel):
    """POST /v1/inference/detect"""
    image_path: str
    confidence_threshold: float = Field(0.5, ge=0.0, le=1.0)
    device: str = Field("cpu")


class Detection(BaseModel):
    class_name: str = Field(..., alias="class")
    confidence: float
    bbox: list[float]

    class Config:
        populate_by_name = True


class InferenceResponse(BaseModel):
    image_path: str
    car_count: int
    detections: list[dict[str, Any]]
    processing_time_ms: float
    worker_id: str
    model: str


# ── Cluster ──────────────────────────────────────────────────────────────────

class NodeInfo(BaseModel):
    node_id: str
    alive: bool
    resources: dict[str, Any] = {}


class ClusterStatusResponse(BaseModel):
    total_cpus: float
    total_gpus: float
    available_cpus: float
    available_gpus: float
    nodes: list[NodeInfo] = []
    queue_depth: int = 0


# ── WebSocket events ─────────────────────────────────────────────────────────

class WSEvent(BaseModel):
    event: str  # job_submitted | job_completed | job_failed
    job_id: str
    data: dict[str, Any] = {}
