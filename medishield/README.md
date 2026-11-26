# MediShield — Healthcare Privacy Firewall

**Yugaantar DevForge Hackathon — Track 3: Secret Wards**  
Offline, CPU-only, LLM-free healthcare privacy firewall for English, Hindi (Devanagari), and Hinglish clinical records.

---

## Key Capabilities
- **Multilingual PII Detection:** Regex, contextual rules, Unicode NFKC normalization, clinical disambiguation (`Dr.`, `C/O fever`, lab numbers), and character-level TF-IDF + Logistic Regression.
- **Keyed Anonymization & Metadata Protection:** Domain-separated HMAC-SHA256 (`RAKSHA_SECRET` + `release_scope`) for pseudonyms, directory names (`dir_`), filenames (`redacted_`), CSV/TSV headers (`field_`), and JSON keys (`key_`).
- **Fail-Safe Quarantine & Clinical Integrity Gate:** Quarantines corrupted/empty/unsupported files without leaking original filenames in `report.json`, and flags any clinical integrity loss (`flagged_clinical_loss`).
- **Authorized Internal Linkage & Privacy Defense Lab:** Strictly separated from public outputs; evaluates distinct-patient $k$-anonymity, unique confident re-ID rate, forced top-match accuracy, and attacker prediction coverage on synthetic data.

---

## Reproducible Offline Installation & Execution

### 1. Backend & CLI Setup (CPU-Only, Offline)
```bash
cd medishield
python3 -m venv backend/.venv
backend/.venv/bin/pip install -r backend/requirements.txt
```

Pinned dependencies (`backend/requirements.txt`):
- `fastapi==0.115.6`, `uvicorn==0.34.0`, `pydantic==2.10.4`
- `scikit-learn==1.6.1`, `numpy==2.2.1`, `pandas==2.2.3`, `rapidfuzz==3.11.0`
- `python-multipart==0.2.0`, `pytest==8.3.4`, `httpx==0.28.1`

### 2. Run Offline CLI (`raksha.toml`)
```bash
# Optional: set release secret for deterministic pseudonyms within a release
export RAKSHA_SECRET="your-release-secret"
./backend/.venv/bin/python main.py --input <input_dir> --output <output_dir>
```

### 3. Run Dashboard (Local Offline)
```bash
# Terminal 1 (Backend)
cd medishield/backend && .venv/bin/uvicorn app.main:app --port 8000

# Terminal 2 (Frontend)
cd medishield/frontend && npm install && npm run build && npm run dev
```

### 4. Frozen Model Checksums (SHA-256)
Verified compatible with `scikit-learn==1.6.1` and `numpy==2.2.1`:
- `backend/artifacts/linkage_model.joblib`: `317c01dc7e970122386183e6033e0801e241908dd27638333231438138f2172f`
- `backend/artifacts/linkage_model_v3.joblib`: `3ed554ef1c510d152c6301cc0136ab77bd38fc81b4788f76063cc450b76c3ff6`
- `backend/artifacts/pii_model.joblib`: `30ed4f909505f35c588e3d8b025e933bee93dd92eb79cbd6363a2748e782f1fd`
- `backend/artifacts/pii_model_v3.joblib`: `30ed4f909505f35c588e3d8b025e933bee93dd92eb79cbd6363a2748e782f1fd`

---

## Documentation
- [Final Release Report](docs/FINAL_RELEASE_REPORT.md)
- [Final Independent Privacy Audit](docs/FINAL_INDEPENDENT_PRIVACY_AUDIT.md)
- [Hackathon Compliance Matrix](docs/HACKATHON_COMPLIANCE_MATRIX.md)
- [Architecture, Brief & Demo Guide](docs/ARCHITECTURE_AND_BRIEF.md)
- [Submission Checklist](docs/FINAL_SUBMISSION_CHECKLIST.md)
- [Viva Preparation Guide](docs/VIVA_PREPARATION.md)
