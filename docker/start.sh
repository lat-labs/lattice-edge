#!/usr/bin/env bash
# start.sh — Start Ray head (if needed) then launch the FastAPI server.
set -euo pipefail

API_PORT="${API_PORT:-8000}"
RAY_ADDRESS="${RAY_ADDRESS:-ray://ray-head:10001}"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║  Lattice Edge — starting services                        ║"
echo "╚══════════════════════════════════════════════════════════╝"

# ── Fix ownership of mounted volumes so the latlab user can write ────────────
echo "→ Fixing permissions on /home/latlab/work ..."
chown -R "${NB_UID:-1000}:${NB_GID:-100}" /home/latlab/work

# ── Drop privileges and launch JupyterLab as the NB_USER ────────────────────
echo "→ Starting JupyterLab as ${NB_USER} ..."
exec gosu "${NB_USER}" jupyter lab \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --NotebookApp.token=''
