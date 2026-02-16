#!/usr/bin/env bash
# start.sh — Start Ray head (if needed) then launch the FastAPI server.
set -euo pipefail

API_PORT="${API_PORT:-8000}"
RAY_ADDRESS="${RAY_ADDRESS:-ray://ray-head:10001}"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║  Lattice Edge — starting services                        ║"
echo "╚══════════════════════════════════════════════════════════╝"

# ── Wait for the external Ray cluster to become reachable ────────────────────
echo "→ Waiting for Ray cluster at ${RAY_ADDRESS} ..."
MAX_RETRIES=30
for i in $(seq 1 $MAX_RETRIES); do
    if python -c "import ray; ray.init(address='${RAY_ADDRESS}', namespace='lattice-detection'); print('ok'); ray.shutdown()" 2>/dev/null; then
        echo "   Ray cluster reachable"
        break
    fi
    if [ "$i" -eq "$MAX_RETRIES" ]; then
        echo "  ✗ Could not reach Ray cluster after ${MAX_RETRIES} attempts"
        exit 1
    fi
    echo "  … attempt $i / $MAX_RETRIES"
    sleep 2
done

# ── Launch FastAPI ───────────────────────────────────────────────────────────
echo "→ Starting Lattice Edge API on port ${API_PORT}"
exec uvicorn api.main:app \
    --host 0.0.0.0 \
    --port "${API_PORT}" \
    --log-level info \
    --ws websockets
