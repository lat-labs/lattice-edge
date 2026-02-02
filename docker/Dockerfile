# DeLab Tier 1: Edge Container
# Minimal Jupyter + Ray client for edge devices and lightweight deployments
FROM python:3.11-slim

# Metadata
LABEL maintainer="DeLab Team <team@delab.io>"
LABEL tier="1-edge"
LABEL description="Minimal DeLab container for edge computing"
LABEL version="1.0.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    JUPYTER_ENABLE_LAB=yes \
    NB_USER=delab \
    NB_UID=1000 \
    NB_GID=100 \
    HOME=/home/delab \
    PATH="/home/delab/.local/bin:${PATH}"

# Create user
RUN useradd -m -s /bin/bash -u ${NB_UID} -g ${NB_GID} ${NB_USER}

# Install minimal system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Switch to user
USER ${NB_USER}
WORKDIR ${HOME}

# Create directory structure
RUN mkdir -p ${HOME}/work \
    ${HOME}/data \
    ${HOME}/.jupyter

# Install minimal Python packages
RUN pip install --no-cache-dir --user \
    jupyterlab>=4.0.0 \
    notebook \
    ipykernel \
    ray[client]==2.10.0 \
    pandas \
    numpy \
    matplotlib \
    requests

# Copy minimal delab core
COPY --chown=${NB_UID}:${NB_GID} delab ${HOME}/delab

# Copy minimal configuration
COPY --chown=${NB_UID}:${NB_GID} config/jupyter_lab_config.py ${HOME}/.jupyter/

# Expose Jupyter port
EXPOSE 8888

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8888/api || exit 1

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''"]