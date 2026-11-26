#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"
VENV_PY="$BACKEND_DIR/.venv/bin/python"
UVICORN_BIN="$BACKEND_DIR/.venv/bin/uvicorn"

echo "=== MediShield Offline Startup ==="

if [[ ! -x "$UVICORN_BIN" ]]; then
  echo "ERROR: Backend venv/uvicorn not found at $UVICORN_BIN"
  echo "Run: cd $ROOT_DIR && python3 -m venv backend/.venv && backend/.venv/bin/pip install -r backend/requirements.txt"
  exit 1
fi

for art in pii_model.joblib linkage_model.joblib pii_model_v3.joblib linkage_model_v3.joblib; do
  if [[ ! -f "$BACKEND_DIR/artifacts/$art" ]]; then
    echo "ERROR: Missing required model artifact: $BACKEND_DIR/artifacts/$art"
    exit 1
  fi
done

check_port() {
  local port="$1"
  if "$VENV_PY" -c "import socket, sys; s=socket.socket(); rc=s.connect_ex(('127.0.0.1', $port)); s.close(); sys.exit(0 if rc != 0 else 1)" 2>/dev/null; then
    return 0
  else
    echo "ERROR: Port $port is already in use. Free port $port manually and retry."
    exit 1
  fi
}

check_port 8000
check_port 5173

BACKEND_PID=""
FRONTEND_PID=""

cleanup() {
  echo ""
  echo "Shutting down MediShield..."
  [[ -n "$FRONTEND_PID" ]] && kill "$FRONTEND_PID" 2>/dev/null || true
  [[ -n "$BACKEND_PID" ]] && kill "$BACKEND_PID" 2>/dev/null || true
  wait 2>/dev/null || true
  echo "Stopped cleanly."
}
trap cleanup EXIT INT TERM

echo "Starting FastAPI backend on http://127.0.0.1:8000 ..."
(cd "$BACKEND_DIR" && "$UVICORN_BIN" app.main:app --host 127.0.0.1 --port 8000 >/tmp/medishield_backend.log 2>&1) &
BACKEND_PID=$!

for i in $(seq 1 30); do
  if "$VENV_PY" -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=1)" 2>/dev/null; then
    echo "Backend healthy!"
    break
  fi
  sleep 0.5
  if [[ "$i" -eq 30 ]]; then
    echo "ERROR: Backend failed health check. See /tmp/medishield_backend.log"
    exit 1
  fi
done

echo "Starting React frontend on http://127.0.0.1:5173 ..."
(cd "$FRONTEND_DIR" && npm run dev -- --host 127.0.0.1 --port 5173 >/tmp/medishield_frontend.log 2>&1) &
FRONTEND_PID=$!

echo "MediShield is running:"
echo "  Dashboard: http://127.0.0.1:5173/"
echo "  API Docs : http://127.0.0.1:8000/docs"
echo "Press Ctrl+C to stop."
wait
