"""FastAPI app — lifespan hooks init Ray, start job monitor, register routers."""

from __future__ import annotations

import logging
import os
from contextlib import asynccontextmanager

import ray
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import job_manager
from api.cluster import router as cluster_router
from api.inference import router as inference_router
from api.jobs import router as jobs_router
from api.stream import router as stream_router

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(name)s  %(levelname)s  %(message)s")
logger = logging.getLogger("api")

RAY_ADDRESS = os.getenv("RAY_ADDRESS", "ray://ray-head:10001")
RAY_NAMESPACE = os.getenv("RAY_NAMESPACE", "lattice-detection")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ── Startup ──────────────────────────────────────────────────────────
    logger.info("Connecting to Ray cluster at %s (namespace=%s)", RAY_ADDRESS, RAY_NAMESPACE)
    ray.init(address=RAY_ADDRESS, namespace=RAY_NAMESPACE)
    logger.info("Ray connected — CPUs: %s  GPUs: %s  Nodes: %d",
                ray.available_resources().get("CPU", 0),
                ray.available_resources().get("GPU", 0),
                len(ray.nodes()))

    job_manager.start_monitor()
    logger.info("Job monitor started")

    yield

    # ── Shutdown ─────────────────────────────────────────────────────────
    job_manager.stop_monitor()
    ray.shutdown()
    logger.info("Ray disconnected")


app = FastAPI(
    title="Lattice Edge API",
    description="Submit detection jobs to the Ray core cluster",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(jobs_router)
app.include_router(inference_router)
app.include_router(stream_router)
app.include_router(cluster_router)


@app.get("/healthz", tags=["health"])
async def healthz():
    return {"status": "ok", "ray_connected": ray.is_initialized()}
