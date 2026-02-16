"""Cluster status endpoint — GPU availability, node info, queue depth."""

from __future__ import annotations

from fastapi import APIRouter

import ray

from api import job_manager
from api.schemas import ClusterStatusResponse, NodeInfo

router = APIRouter(prefix="/v1/cluster", tags=["cluster"])


@router.get("/status", response_model=ClusterStatusResponse)
async def cluster_status():
    resources = ray.cluster_resources()
    available = ray.available_resources()

    nodes = []
    for node in ray.nodes():
        nodes.append(NodeInfo(
            node_id=node.get("NodeID", ""),
            alive=node.get("Alive", False),
            resources=node.get("Resources", {}),
        ))

    return ClusterStatusResponse(
        total_cpus=resources.get("CPU", 0),
        total_gpus=resources.get("GPU", 0),
        available_cpus=available.get("CPU", 0),
        available_gpus=available.get("GPU", 0),
        nodes=nodes,
        queue_depth=job_manager.queue_depth(),
    )
