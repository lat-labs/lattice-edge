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
COPY --chown=${NB_UID}:${NB_GID} latlab-theme ${HOME}/latlab-theme

# Copy minimal configuration
COPY --chown=${NB_UID}:${NB_GID} config/jupyter_lab_config.py ${HOME}/.jupyter/

# Copy favicon into JupyterLab's static directory and page_config for app name
COPY --chown=${NB_UID}:${NB_GID} config/page_config.json ${HOME}/page_config.json
COPY --chown=${NB_UID}:${NB_GID} config/favicon.ico ${HOME}/favicon.ico

# Build and install the prebuilt JupyterLab theme extension
RUN cd ${HOME}/latlab-theme \
    && npm install \
    && npm run build \
    && jupyter labextension build . \
    && python - <<'PY'
from pathlib import Path
from shutil import rmtree, copytree
from jupyter_core.paths import jupyter_data_dir

root = Path("/home/latlab/latlab-theme")
candidates = list(root.rglob("remoteEntry*.js"))
if not candidates:
    raise SystemExit("Could not find built labextension output")

extension_dir = candidates[0].parent.parent
dst = Path(jupyter_data_dir()) / "labextensions" / "@latlab" / "theme-latlab-dark"

if dst.exists():
    rmtree(dst)
copytree(extension_dir, dst)
PY

# Set latlab Dark as the default theme
RUN python - <<'PY'
from pathlib import Path

settings_dir = Path("/home/latlab/.jupyter/lab/user-settings/@jupyterlab/apputils-extension")
settings_dir.mkdir(parents=True, exist_ok=True)
settings_file = settings_dir / "themes.jupyterlab-settings"

settings_file.write_text('{\n  "theme": "latlab Dark"\n}')
PY

# Set custom app name ("latlab") and favicon
RUN python - <<'PY'
from pathlib import Path
import shutil, json
from jupyterlab.commands import get_app_dir

lab_app_dir = Path(get_app_dir())

# -- page_config.json: sets the tab title --
page_config_dir = lab_app_dir / "settings"
page_config_dir.mkdir(parents=True, exist_ok=True)
page_config_file = page_config_dir / "page_config.json"

existing = {}
if page_config_file.exists():
    existing = json.loads(page_config_file.read_text())
custom = json.loads(Path("/home/latlab/page_config.json").read_text())
existing.update(custom)
page_config_file.write_text(json.dumps(existing, indent=2))

# -- favicon: replace the default Jupyter favicon --
static_dir = lab_app_dir / "static" / "favicons"
static_dir.mkdir(parents=True, exist_ok=True)
favicon_src = Path("/home/latlab/favicon.ico")
if favicon_src.exists():
    shutil.copy2(favicon_src, static_dir / "favicon.ico")

    # Also replace in jupyter_server's static dirs (where the browser actually loads it)
    import jupyter_server
    server_static = Path(jupyter_server.__file__).parent / "static"
    for target in [
        server_static / "favicon.ico",
        server_static / "favicons" / "favicon.ico",
    ]:
        if target.parent.exists():
            shutil.copy2(favicon_src, target)
PY

# Expose Jupyter port
EXPOSE 8888

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8888/api || exit 1

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''"]