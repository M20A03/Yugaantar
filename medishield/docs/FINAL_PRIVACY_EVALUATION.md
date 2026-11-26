# MediShield — Final Privacy & Re-Identification Evaluation

## 1. Executive Summary
MediShield was evaluated offline on CPU across all four synthetic hospital systems (`Apex_HIS`, `Bharat_Care`, `Swasthya_Clinic`, `Metro_Diagnostics`) against a synthetic voter-list re-identification attacker, alongside metadata leakage, clinical preservation, and fail-safe quarantine tests.

All 10 automated backend tests pass (`pytest -v backend/tests`) and the React + TypeScript dashboard builds cleanly (`npm run build`).

---

## 2. Defensive Re-Identification Resistance Lab (4-System Cohort vs. Synthetic Voter List)

Measured via `POST /privacy-defense/evaluate?n_patients=36&seed=42` (`reid_lab.py`):

| Metric | Observed Result |
|---|---|
| Total fragmented records | 87 (across 36 synthetic patients & 4 hospital systems) |
| Synthetic voter list size | 60 (36 patients + 24 distractors) |
| Attacker Re-ID rate **before** MediShield | **100.0%** (87 / 87 records) |
| Attacker Re-ID rate **after** MediShield | **0.0%** (0 / 87 records) |
| Risk reduction | **100.0%** |
| Direct PII leakage rate | **0.0%** (0 leaks across all 4 systems) |
| Minimum anonymity group size ($k$) | **2** |
| Average anonymity group size ($k$) | **7.91** |
| Residual quasi-identifier exposure score | **0.171** (Low risk) |
| Clinical preservation score | **100.0%** (1.0) |
| End-to-end CPU latency (87 records) | **146.87 ms** |

### Per-Hospital Breakdown
| Hospital System | Language / Format | Records | Before Re-ID | After Re-ID | Direct PII Leaks |
|---|---|---|---|---|---|
| `Apex_HIS` | English structured | 25 | 25 | 0 | 0 |
| `Bharat_Care` | Hinglish mixed | 20 | 20 | 0 | 0 |
| `Swasthya_Clinic` | Hindi (Devanagari) | 20 | 20 | 0 | 0 |
| `Metro_Diagnostics` | Abbreviated / missing phone | 22 | 22 | 0 | 0 |

> Note: During initial testing, `Bharat_Care` surfaced 20 direct PII leaks because the Hinglish keyword `Mariz` was missing from `PATIENT_PREFIX_RE` in `detector.py`. Adding `Mariz` reduced direct PII leakage to **0.0%** across all four systems.

---

## 3. Clinical Integrity Verification
Verified in `test_clinical_integrity_preserves_units_labs_vitals_and_stay` (`fidelity.py`):
- **Medications & Dosages:** `Metformin 500 mg 1-0-1`, `Insulin 10 units BD` — **100% preserved**
- **Laboratory Values & Units:** `HbA1c 7.8%`, `Creatinine 1.2 mg/dL` — **100% preserved**
- **Vital Measurements:** `BP 130/85 mmHg` — **100% preserved**
- **Hospital Stay Lengths:** `4 days`, `3 days` — **100% preserved**

---

## 4. Metadata Sanitization & Fail-Safe Quarantine
Verified in `test_cli_metadata_sanitization_and_quarantine` (`main.py`):
- **Directory names with PII** (e.g., `Aarav_Sharma_9876543210/`) -> replaced with `dir_<sha256[:8]>`.
- **Filenames with PII** (e.g., `Rahul_Verma_9811223344.txt`) -> renamed to `redacted_<sha256[:8]>.txt`.
- **CSV/TSV column headers with PII** -> replaced with collision-safe `field_<sha256[:8]>`.
- **JSON keys with PII** -> replaced with collision-safe `key_<sha256[:8]>` (appending `_2`, etc. on collision so no clinical values are overwritten).
- **Quarantined inputs** (invalid UTF-8 bytes, empty `.txt`, broken `.json`, `.exe`, malformed `.csv` rows) -> quarantined with `output: None` and never copied into `sanitized/` or exposed by original name in `report.json`.

---

## 5. Frozen Model Preservation
The existing trained artifacts in `medishield/backend/artifacts/` (`pii_model.joblib`, `linkage_model.joblib`, `pii_model_v3.joblib`, `linkage_model_v3.joblib`) were preserved untouched.
