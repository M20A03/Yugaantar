# MediShield — Release Certification Report

**Audit Date:** 2026-11-26  
**Candidate Branch:** `main` (see `git log -1` after this commit)  
**Model Artifacts Status:** Frozen & Untouched

---

## 1. Exact Automated Test Results (Observed)
- **Backend & QA Suite (`./backend/.venv/bin/pytest -v backend/tests`):** **16/16 passed** in `2.24s` (zero skipped, zero relaxed assertions).
- **Frontend Production Build (`cd frontend && npm run build`):** **Passed** in `1.82s` (`tsc && vite build`, `dist/assets/index-D4rUlhNw.js`).
- **Two-Page Brief PDF (`docs/MediShield_Project_Brief.pdf`):** **2 pages** verified via `pdfinfo` and visually inspected via `pdftoppm`.

---

## 2. Record Linkage 240-Pair Metric Audit (`training/release_certification_eval.py`)
Clarifying the 240-pair evaluation (`80` true positives + `80` shared-family-phone negatives + `80` distinct negatives):
- **Actual Positives:** `80` | **Actual Negatives:** `160`
- **True Positives (TP):** `80` | **True Negatives (TN):** `80`
- **False Positives (FP):** `0` | **False Negatives (FN):** `0`
- **Reviewed Positives:** `0` | **Reviewed Negatives:** `80` (all 80 shared-family-phone pairs routed to `uncertain_review`)
- **Automatic Decision Coverage:** `160 / 240 = 66.67%`
- **Selective F1 (on automatically decided cases):** `1.0000`
- **Overall Automatic-Match Precision / Recall / F1:** `1.0000` / `1.0000` / `1.0000`

---

## 3. Independent Frozen Challenge Results (`training/release_certification_eval.py`)
Evaluated with frozen sanitizer & models (no tuning against challenge):
- **PII Stripping:** **5/6** passed (`visited zoya qureshi`, `follow up for devansh bajpai`, `Patient आरव शर्मा (Aarav Sharma)`, nested JSON `patient_rohan_mehta` + phone, `Patient Neha Gupta`).
- **Genuine Failure Reported:** `please check on tanmay chatterjee today, BP 130/85 mmHg` -> missed (`tanmay` not in lexicon and `"check on"` not in prepositional cues).
- **Clinical Preservation:** **7/7 (100%)** (`Metformin 500 mg`, `HbA1c 7.8%`, `BP 130/85 mmHg`, `SpO2 95%`, `Warfarin 2.5 mg`, `Platelets 145000 /uL`, `Rosuvastatin 10 mg` & `Aspirin 75 mg`).
- **Conservative Redaction Note:** `Specimen 9812345670` (10 digits starting with `9` without clinical unit) was redacted as `[PHONE_REDACTED]`.
- **Shared Phone + Missing Demographics:** `0` false auto-clusters.
- **CLI Quarantine & Completeness:** `files_total=2`, `files_sanitized=1`, `files_quarantined=1`, `output_completeness=0.5`.

---

## 4. Offline Execution & Repository Security Verification
- **Offline Execution:** Verified `pytest`, `npm run build`, `python main.py` CLI, and `release_certification_eval.py` with zero external network calls (sandboxed offline execution).
- **Repository Cleanliness:** `REPO_CLEAN_NO_SECRETS_OR_CACHES` (`git ls-files` contains zero `.env`, key, token, or `__pycache__` files).
- **Frozen Model SHA-256 Checksums:**
  - `backend/artifacts/linkage_model.joblib`: `317c01dc7e970122386183e6033e0801e241908dd27638333231438138f2172f`
  - `backend/artifacts/linkage_model_v3.joblib`: `3ed554ef1c510d152c6301cc0136ab77bd38fc81b4788f76063cc450b76c3ff6`
  - `backend/artifacts/pii_model.joblib`: `30ed4f909505f35c588e3d8b025e933bee93dd92eb79cbd6363a2748e782f1fd`
  - `backend/artifacts/pii_model_v3.joblib`: `30ed4f909505f35c588e3d8b025e933bee93dd92eb79cbd6363a2748e782f1fd`

---

## 5. Official Compliance & 15-Point Readiness Tracker
- **Official Validator (`validate_output.py`), Submission Schema & Eligibility Rules:** **PENDING — ORGANIZER CONFIRMATION REQUIRED** (confirm original-work, AI-assisted development, and pre-trained model reuse rules before official submission).
- **Readiness Tracker:**
  - Items 1–12 (Architecture, ML pipeline, Working UI/Backend, Adversarial audit, Metadata privacy, Clinical integrity, Privacy Defense Lab, Project brief, Demo guide, Clinical release blocking, Lowercase PII hardening, 2-page PDF): **PASSED** (with documented unprefixed unfamiliar lowercase limitation).
  - Item 13 (Official validator & eligibility): **PENDING**
  - Items 14–15 (Personal viva preparation & live demo rehearsal): **REQUIRES MANUAL PRACTICE**
