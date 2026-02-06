# latlab Tier 1: Edge Container
# Minimal Jupyter + Ray client for edge devices and lightweight deployments
FROM python:3.11-slim

# Metadata
LABEL maintainer="latlab Team <team@latlab.io>"
LABEL tier="1-edge"
LABEL description="Minimal latlab container for edge computing"
LABEL version="1.0.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    JUPYTER_ENABLE_LAB=yes \
    NB_USER=latlab \
    NB_UID=1000 \
    NB_GID=100 \
    HOME=/home/latlab \
    PATH="/home/latlab/.local/bin:${PATH}"

# Create user
RUN useradd -m -s /bin/bash -u ${NB_UID} -g ${NB_GID} ${NB_USER}

# Install minimal system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    nodejs \
    npm \
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

# Copy minimal latlab core
COPY --chown=${NB_UID}:${NB_GID} latlab ${HOME}/latlab

# Copy theme installer and theme extension source
COPY --chown=${NB_UID}:${NB_GID} theme.py ${HOME}/theme.py
COPY --chown=${NB_UID}:${NB_GID} delab-theme ${HOME}/delab-theme

# Copy minimal configuration
COPY --chown=${NB_UID}:${NB_GID} config/jupyter_lab_config.py ${HOME}/.jupyter/

# Build and install the prebuilt JupyterLab theme extension
RUN cd ${HOME}/delab-theme \
    && npm install \
    && npm run build \
    && jupyter labextension build . \
    && python - <<'PY'
from pathlib import Path
from shutil import rmtree, copytree
from jupyter_core.paths import jupyter_data_dir

root = Path("/home/latlab/delab-theme")
candidates = list(root.rglob("remoteEntry*.js"))
if not candidates:
    raise SystemExit("Could not find built labextension output")

extension_dir = candidates[0].parent.parent
dst = Path(jupyter_data_dir()) / "labextensions" / "@delab" / "theme-delab-dark"

if dst.exists():
    rmtree(dst)
copytree(extension_dir, dst)
PY

# Set DeLab Dark as the default theme
RUN python - <<'PY'
from pathlib import Path

settings_dir = Path("/home/latlab/.jupyter/lab/user-settings/@jupyterlab/apputils-extension")
settings_dir.mkdir(parents=True, exist_ok=True)
settings_file = settings_dir / "themes.jupyterlab-settings"

settings_file.write_text('{\n  "theme": "DeLab Dark"\n}')
PY

# Expose Jupyter port
EXPOSE 8888

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8888/api || exit 1

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''"]