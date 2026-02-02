# Lattice - Federated Research Platform

**Multi-user JupyterHub deployment for collaborative biological machine learning research with GPU support and distributed computing.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![JupyterHub](https://img.shields.io/badge/JupyterHub-5.4-orange.svg)](https://jupyter.org/hub)

## Overview

DeLab is a research platform that enables collaborative biological discovery through distributed computing. It provides a three-tier architecture (L1 Edge → L2 Workstation → L3 Datacenter) with multi-user JupyterHub, GPU acceleration, and Ray cluster integration.

### Key Features

- **Multi-User JupyterHub** - Isolated environments with profile-based container selection
- **GPU Support** - NVIDIA GPU acceleration for computational biology workloads
- **Ray Clustering** - Distributed computing for large-scale BioML tasks
- **Custom Extensions** - Specialized JupyterLab extensions for biological research
- **Federated Architecture** - Three-tier deployment (Edge / Workstation / Datacenter)
- **Data Sovereignty** - User data isolation with shared model/dataset access

## Quick Start

### Prerequisites

- Docker 24.0+ with nvidia-runtime
- Docker Compose 2.0+
- NVIDIA GPUs (optional but recommended)
- 32GB+ RAM recommended
- Linux server (tested on Ubuntu 22.04)

### Installation

```bash
# Clone the repository
git clone https://github.com/lat-labs/lattice-edge
cd lattice-edge

# Set up configuration
cd config
cp .env.example .env
# Edit .env with your settings

# Build and start services
docker compose up -d

# Check status
docker compose ps
docker compose logs -f jupyterhub
```

### Accessing JupyterHub

- **Local:** http://localhost:8080
