# MediShield — Master Development Plan (Grand Finale)

## 1. Repository Audit Summary
- **Working Core:** FastAPI backend (`backend/app/`), React 18 + TypeScript + Tailwind + Recharts light-theme UI (`frontend/`), offline CLI (`main.py`), frozen V2/V3 `.joblib` artifacts (`backend/artifacts/`), SQLite `AuditStore`.
- **Critical Weaknesses Identified:**
  1. **Unprefixed Lowercase Names:** `detector.py` misses `"met rahul sharma yesterday"`, `"spoke with ananya kulkarni"`, `"ravi kumar was brought"`, `"kal priya singh hospital aayi thi"`.
  2. **Raw JSON in Text API:** `/scan` and `/anonymize` treat serialized JSON strings as flat text instead of routing through key-aware structural sanitization.
  3. **Clinical Integrity Gate:** `main.py` flags `flagged_clinical_loss` in `report.json` but still writes the corrupted file to `sanitized/` instead of attempting safe recovery and withholding on failure.
  4. **Shared-Family-Phone Linkage:** Frozen V3 model over-predicts on shared family phones with different first names; needs explicit post-model decision policy guardrails.
  5. **Dashboard Coverage & Explainability:** Needs **Metadata Security** (10th tab), **Explainability Panel**, **Clinical Integrity Inspector**, **Cohort Selector (100–5,000)** in Privacy Defense Lab, and **Live Demonstration Mode**.

## 2. Prioritized Implementation Schedule
1. **Priority 1 (Privacy & Compliance):** Lowercase/multilingual PII detection + shared structural JSON/CSV/TSV/TXT sanitizer + fail-closed clinical integrity gate + security hardening (depth/size/traversal guards).
2. **Priority 2 (Defense & Linkage):** Privacy Defense Lab V2 (100–5,000 cohorts, random-guess baseline, distinct-patient $k$-anonymity) + safe 3-outcome record linkage policy.
3. **Priority 3 (Dashboard & Demo):** 10-tab light clinical UI with side-by-side diff, Explainability Panel, Metadata Security Inspector, and curated Live Demo Mode.
4. **Priority 4 (QA, Profiling & Docs):** CPU stage-by-stage profiling, expanded `pytest` suite, clean offline CLI check, 2-page `MediShield_Project_Brief.pdf`, `FINAL_VIVA_MASTER_GUIDE.md`, `FINAL_DEMO_SCRIPT.md`, and `FINAL_RELEASE_REPORT.md`.
