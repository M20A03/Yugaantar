# MediShield — Emergency Demonstration Backup Kit

Use this kit if live internet is unavailable or if the browser UI fails during judging.

## 1. One-Command Startup (Linux/macOS)
```bash
cd medishield
./start_medishield.sh
```
- **Dashboard:** `http://127.0.0.1:5173/`
- **Backend API:** `http://127.0.0.1:8000/docs`

## 2. Manual Startup Backup (Two Terminals)
```bash
# Terminal 1 (Backend)
cd medishield/backend && .venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000

# Terminal 2 (Frontend Production Preview - Offline)
cd medishield/frontend && npm run preview -- --host 127.0.0.1 --port 5173
```

## 3. Instant CLI Fallback Demo (Zero Browser Needed)
```bash
cd medishield
./backend/.venv/bin/python main.py --input backup_kit/demo_inputs --output /tmp/medishield_demo_out
cat /tmp/medishield_demo_out/report.json
```

## 4. Quick Pre-Judging Health & Battle Check
```bash
cd medishield
./backend/.venv/bin/pytest -q backend/tests
./backend/.venv/bin/python scripts/run_live_battle_test.py --mode quick
```

## 5. Troubleshooting
- **Port 8000/5173 occupied:** Run on alternate ports (`--port 8001` / `--port 5174`) or stop your previous dev server cleanly.
- **UI blank or API unreachable:** Run the CLI fallback command above to demonstrate sanitization, metadata protection, clinical integrity, and quarantine directly in the terminal.
