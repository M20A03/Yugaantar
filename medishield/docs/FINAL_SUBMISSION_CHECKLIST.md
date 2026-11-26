# MediShield — Final Hackathon Submission Checklist (Track 3: Secret Wards)

## 1. Track 3 Constraints & Runtime Verification
- [x] **Offline CPU-Only Execution:** Verified via `GET /health` (`offline_mode: true`, `llm_usage: false`) and offline CLI `python main.py --input <dir> --output <dir>`.
- [x] **Zero LLM / Foundation Model Inference:** Uses only Regex, Contextual Rules, Char TF-IDF + Logistic Regression, RapidFuzz, and GradientBoosting / LogisticRegression record linkage.
- [x] **No Custom Cryptography:** Uses Python stdlib `hashlib.sha256` and `hmac` (`AnonymizerEngine._derive_release_key` & `opaque_metadata_id`).
- [x] **Frozen Model Artifacts Preserved:** `backend/artifacts/pii_model.joblib`, `linkage_model.joblib`, `pii_model_v3.joblib`, `linkage_model_v3.joblib` untouched.
- [x] **Official Validator Status:** `validate_output.py` and official organizer dataset are **not present** in the workspace (`Requires official clarification`). No synthetic script is labeled as an official validator.

## 2. Dependency & Installation Verification
Verified in `medishield/raksha.toml` and `medishield/backend/requirements.txt`:
- `setup = "pip install -r backend/requirements.txt"`
- `run = "python main.py --input {input} --output {output}"`
- Pinned versions in `backend/requirements.txt`: `fastapi==0.115.6`, `uvicorn==0.34.0`, `pydantic==2.10.4`, `rapidfuzz==3.11.0`, `scikit-learn==1.6.1`, `numpy==2.2.1`, `pandas==2.2.3`, `python-multipart==0.0.20`, `pytest==8.3.4`, `httpx==0.28.1` (`joblib` installed with `scikit-learn`).

## 3. Security, Privacy & Integrity Verification
- [x] **Secret-Key & Release-Scope Isolation:** Verified in `final_submission_audit.py` (`ephemeral_keys_isolated: true`, `release_scope_isolated: true`). Set `RAKSHA_SECRET` in production/submission environments if cross-process deterministic pseudonyms within a release are needed; otherwise an ephemeral 256-bit key is generated per instance.
- [x] **Metadata Sanitization & Fail-Safe Quarantine:** Verified in `test_cli_metadata_sanitization_and_quarantine` (`main.py` sanitizes directory names, filenames, CSV/TSV headers, and JSON keys with collision-safe keyed HMAC tokens, and quarantines corrupted/empty/unsupported files without leaking original filenames in `report.json`).
- [x] **Clinical Integrity:** **100.0%** exact preservation across 5,000 synthetic examples and 210 handwritten records (medications, dosages, labs, vitals, hospital stay lengths, doctor names, `C/O` complaints).
- [x] **Distinct-Patient vs. Record-Level $k$-Anonymity:** Audited and documented honestly (`record_level_min_k = 2` vs `distinct_patient_min_k = 1` when one patient has multiple hospital records).
- [x] **Backend Tests & Frontend Build:** `pytest -v backend/tests` (**10/10 passed**) and `cd frontend && npm run build` (**passed**).
