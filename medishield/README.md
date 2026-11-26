# MediShield — Healthcare Privacy Firewall

**Tagline:** Protecting Identities. Preserving Medical Intelligence.

Offline, LLM-free healthcare privacy firewall for fragmented synthetic hospital records in **English, Hindi (Devanagari), and Hinglish**.

## Architecture
- **Backend (`backend/app/`):** FastAPI + Pydantic v2 + Regex + Devanagari-to-Latin transliteration + contextual disambiguation + `scikit-learn` TF-IDF/LogisticRegression context classifier + `RapidFuzz` cross-hospital record linkage + *k*-anonymity risk analysis + medical data fidelity scoring + sanitized-only SQLite audit metadata.
- **Frontend (`frontend/`):** React 18 + TypeScript + Vite + Tailwind CSS + Recharts dark navy/teal enterprise dashboard (`Overview`, `Record Scanner`, `Batch Processing`, `Privacy Risk Analysis`, `Record Linkage`, `Medical Fidelity`, `Audit Logs`, `Evaluation Lab`, `Settings`).
- **Offline CLI (`raksha.toml` + `main.py`):** Processes directories of `.csv`, `.tsv`, `.json`, and `.txt` records with zero internet access, outputting `sanitized/`, `report.json`, and `records.jsonl`.

## Quick Start (Offline)

### 1. Backend
```bash
cd medishield/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### 2. Frontend
```bash
cd medishield/frontend
npm install
npm run dev
```
Open `http://localhost:5173`.

### 3. Run Tests & Offline CLI
```bash
cd medishield
./backend/.venv/bin/pytest -v backend/tests
./backend/.venv/bin/python main.py --input data/synthetic --output /tmp/medishield_out
```

## API Endpoints
- `GET /health`
- `POST /scan`
- `POST /anonymize`
- `POST /batch-process`
- `POST /linkage/analyze`
- `POST /risk/analyze`
- `POST /fidelity/evaluate`
- `GET /metrics`
- `GET /evaluation/run`

See [`docs/ARCHITECTURE_AND_SPECS.md`](./docs/ARCHITECTURE_AND_SPECS.md) for the full PRD, TRD, UI/UX design document, backend schema, and research notes.
