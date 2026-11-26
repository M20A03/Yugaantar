# MediShield — Complete Documentation

Everything you need for **MediShield — Healthcare Privacy Firewall** (*Yugaantar DevForge Track 3: Secret Wards*) in one clean file, alongside the 2-page PDF brief ([MediShield_Project_Brief.pdf](MediShield_Project_Brief.pdf)).

---

## 1. Quick Overview & Architecture
- **Goal:** Offline, CPU-only, LLM-free privacy firewall for English, Hindi (Devanagari), and Hinglish clinical records scattered across 4 hospital systems.
- **Public Firewall (`main.py` & `/anonymize`, `/batch-process`):**
  1. **Fail-Safe Quarantine Gate:** Rejects symlinks, oversized files (`>10 MB`), broken UTF-8, empty files, malformed CSV/TSV, invalid/deep JSON (`>32` levels), and unsupported extensions (`.exe`, etc.) — logged by SHA-256 only, never copied to `sanitized/`.
  2. **Keyed Metadata Sanitizer (`anonymizer.py`):** Uses domain-separated HMAC-SHA256 (`RAKSHA_SECRET` + `release_scope`) to replace PII in directory names (`dir_`), filenames (`redacted_`), CSV/TSV headers (`field_`), and JSON keys (`key_`) with collision-safe suffixes.
  3. **Multilingual PII Detector (`detector.py`):** Unicode NFKC normalization + regex + sliding-window Indian name pairs + English/Hinglish/Hindi context rules + frozen char TF-IDF & Logistic Regression. Protects `Dr.` names, `C/O fever`, `Parkinson's disease`, `Wilson's disease`, and `"marez was admitted"`.
  4. **Independent Privacy Verifier & Fail-Closed Clinical Gate (`release_gate.py`, `fidelity.py`):** Second-pass residual PII check + exact preservation check for medications, decimal dosages, units, labs, vitals, and stay lengths. Attempts safe recovery on collision or withholds/quarantines unresolved outputs (`422` / `quarantined_clinical_loss`).
- **Authorized Internal-Only Modules (Separated from Public Outputs):**
  - **Cross-Hospital Record Linkage (`linker.py`):** Frozen V2/V3 models + RapidFuzz with a shared-family-phone + distinct-first-name guardrail (routes ambiguous family-phone pairs to `uncertain_review`).
  - **Privacy Defense Lab (`reid_lab.py`):** Synthetic 4-hospital vs. voter-list simulation measuring distinct-patient $k$-anonymity (never counting duplicate hospital rows as distinct people).

---

## 2. Official Compliance & Readiness Status
- **Offline CPU-only, zero LLM inference, no custom crypto:** **PASSED**
- **16/16 Backend & QA Tests (`pytest -v backend/tests`):** **PASSED**
- **Frontend Production Build (`npm run build`, 10-tab light clinical UI):** **PASSED**
- **2-Page Project Brief PDF (`MediShield_Project_Brief.pdf`):** **PASSED (2 pages)**
- **Official Organizer Validator (`validate_output.py`):** **PENDING — ORGANIZER CONFIRMATION REQUIRED** (not present in workspace).
- **Personal Viva & Demo Rehearsal:** **REQUIRES MANUAL PRACTICE**

---

## 3. Observed Synthetic Benchmarks & Honest Limitations
> **Important:** Observed `0.0%` direct PII leakage and `100.0%` clinical preservation apply **only** to the evaluated synthetic benchmarks, not a guarantee on all real-world data.

- **Lowercase & Unfamiliar Names Challenge (15 cases, incl. medical traps):** Precision `1.0` (`FP=0`), Recall `1.0` (`FN=0`), F1 `1.0`, Clinical Preservation `1.0`.
- **210 Handwritten Synthetic Records:** `100.0%` PII strip and `100.0%` clinical preservation across all 5 categories (`standard_multilingual`, `unprefixed_lowercase_names`, `nested_identifiers`, `ambiguous_medical_values`, `unfamiliar_multilingual_phrases`).
- **Large-Scale Sealed Cohorts (100–5,000 synthetic patients):** `0.0%` direct PII leakage, `0.0%` unique confident re-ID, `100%` attacker coverage, forced top-match accuracy `11.14%` ($N=100$) down to `0.24%` ($N=5,000$).
- **Policy Optimization (500 synthetic patients):** `10-year` age band selected as default (`2.30%` forced top-match vs. `0.19%` random-guess baseline, `distinct_patient_min_k = 33`, `avg_k = 41.67`).
- **240-Pair Linkage Regression:** `80/80 TP`, `0/80 FP` on shared-family-phone negatives (all 80 routed to `uncertain_review`), `80/80 TN`, `auto_F1 = 1.0`.
- **CPU Performance:** In-memory (`1,000` records): `89.71 ms` load, `0.364 ms` avg (`P95 0.67 ms`), `2,737.5 rec/sec`, `174.95 MB` RAM. File-to-file CLI (`200` mixed `.txt`/`.json` files): `927.6 files/sec`, `1.08 ms/file`, `188.59 MB` RAM.
- **Known Limitations:** Completely unfamiliar lowercase names without context cues or lexicon match can still be missed; 10-year age bands and gender remain as residual quasi-identifiers ($\approx 1/k$ forced-guess accuracy).

---

## 4. Frozen Model Checksums (SHA-256)
- `backend/artifacts/linkage_model.joblib`: `317c01dc7e970122386183e6033e0801e241908dd27638333231438138f2172f`
- `backend/artifacts/linkage_model_v3.joblib`: `3ed554ef1c510d152c6301cc0136ab77bd38fc81b4788f76063cc450b76c3ff6`
- `backend/artifacts/pii_model.joblib`: `30ed4f909505f35c588e3d8b025e933bee93dd92eb79cbd6363a2748e782f1fd`
- `backend/artifacts/pii_model_v3.joblib`: `30ed4f909505f35c588e3d8b025e933bee93dd92eb79cbd6363a2748e782f1fd`

---

## 5. Live Demo Script (2–3 Minutes)
1. **Start Offline:** Backend `.venv/bin/uvicorn app.main:app --port 8000` + Frontend `npm run dev`.
2. **Record Scanner:** Run **Demo 1: Hinglish**, **Demo 3: Lowercase** (`met rahul sharma...`), and **Demo 4: JSON String** — show side-by-side comparison, Explainability Summary, and `100%` Medical Fidelity.
3. **Metadata Security Tab:** Click **Inspect Metadata** — show keyed HMAC tokens (`redacted_`, `dir_`, `field_`, `key_`), traversal blocking, and quarantine rules.
4. **Privacy Defense Lab:** Select **1,000 patients / 10-yr age band** — show `0.0%` Unique Confident Re-ID, Forced Top-Match Accuracy, Distinct-Patient $k$, and Remaining Limitations.
5. **Offline CLI:** Run `python main.py --input <in> --output <out>` and inspect `report.json`.

---

## 6. Quick Viva Q&A (Simple English)
- **Why not use an LLM?** Track 3 requires offline, CPU-only execution with zero LLMs or external APIs. Classical ML + rules run in `<1 ms` per record on CPU.
- **Why HMAC-SHA256 instead of plain SHA-256?** Unkeyed SHA-256 can be reversed with a dictionary of common names/headers and links files across releases. Keyed HMAC-SHA256 with `release_scope` stops both.
- **Why distinct-patient $k$-anonymity?** Counting hospital rows tricks you when 1 patient visits 3 hospitals (looks like $k=3$ when there is only 1 person). Deduplicating by `patient_id` gives the true anonymity group size.
- **What if clinical data gets damaged?** Our fail-closed Clinical Release Gate checks medicines, dosages, labs, vitals, and stay lengths. If anything is lost and safe recovery fails, it blocks/quarantines the output rather than releasing corrupted medical data.
