# Lattice - Federated Research Platform

**Multi-user JupyterHub deployment for collaborative biological machine learning research with GPU support and distributed computing.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![JupyterHub](https://img.shields.io/badge/JupyterHub-5.4-orange.svg)](https://jupyter.org/hub)

## Overview

latlab is a research platform that enables collaborative biological discovery through distributed computing. It provides a three-tier architecture (L1 Edge → L2 Workstation → L3 Datacenter) with multi-user JupyterHub, GPU acceleration, and Ray cluster integration.

### Key Features

- **Multi-User JupyterHub** - Isolated environments with profile-based container selection
- **GPU Support** - NVIDIA GPU acceleration for computational biology workloads
- **Ray Clustering** - Distributed computing for large-scale BioML tasks
- **Custom Extensions** - Specialized JupyterLab extensions for biological research
- **Federated Architecture** - Three-tier deployment (Edge / Workstation / Datacenter)
- **Data Sovereignty** - User data isolation with shared model/dataset access

## Quick Start

### Prerequisites

- Docker 24.0+
- Docker Compose 2.0+

## 1. Pull the Jupyter image
`docker pull logan422/lattice-edge:main`

## 2. Run the container
`docker run -d \
  --name lattice-edge \
  --network lattice-network \
  -p 8889:8889 \
  logan422/lattice-edge:main`

## 3. Access Jupyter
Once the container starts, navigate to 
 **URL**: http://localhost:8889

## Stopping the container
`docker stop lattice-edge`
## Removing the container
`docker rm lattice-edge`

### Run

```bash
# Clone the repository
git clone https://github.com/lat-labs/lattice-edge
cd lattice-edge


# Add a docker network

docker network create lattice-network

# Build and start the container
docker compose --profile edge up -d

# Check status
docker compose ps
```

### Accessing JupyterLab

- **URL:** http://localhost:8889


