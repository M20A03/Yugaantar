# MediShield — Hackathon Compliance Matrix (Yugaantar DevForge Track 3: Secret Wards)

| Requirement | Status | Source File(s) | Test Evidence | Notes |
|---|---|---|---|---|
| Offline CPU-only, zero LLM inference | Passed with test evidence | `main.py`, `detector.py`, `linker.py` | `test_health`, `final_submission_audit.py` | Zero external APIs; frozen scikit-learn + RapidFuzz models. |
| No custom cryptography | Passed with test evidence | `anonymizer.py`, `main.py` | `test_cli_metadata_sanitization_and_quarantine` | Uses Python stdlib `hmac` + `hashlib.sha256` only. |
| Multilingual PII (English, Hindi, Hinglish, lowercase) | Partially implemented | `detector.py` | `test_privacy_and_quarantine.py` | Upgrading lowercase & mixed-script detection in Phase 2. |
| Universal structured sanitization (TXT/CSV/TSV/JSON) | Partially implemented | `main.py`, `routes.py` | `test_cli_metadata_sanitization_and_quarantine` | Sharing structural JSON sanitizer with API in Phase 3. |
| Fail-closed clinical integrity gate | Partially implemented | `fidelity.py`, `main.py` | `test_clinical_integrity_preserves_units_labs_vitals_and_stay` | Upgrading from flag-only to recover-or-withhold in Phase 4. |
| Distinct-patient anonymity & Privacy Defense Lab | Passed with test evidence | `reid_lab.py` | `test_privacy_defense_lab_endpoint` | Upgrading to cohorts 100–5,000 + random baseline in Phase 7. |
| Safe 3-way internal record linkage | Partially implemented | `linker.py` | `test_cross_hospital_record_linkage` | Hardening shared-family-phone guardrail in Phase 8. |
| Metadata protection & fail-safe quarantine | Passed with test evidence | `main.py`, `anonymizer.py` | `test_cli_metadata_sanitization_and_quarantine` | Keyed HMAC metadata IDs + SHA-256-only quarantine logs. |
| Official `validate_output.py` & scoring contract | Pending organizer clarification | `raksha.toml`, `docs/OFFICIAL_COMPLIANCE.md` | — | Official validator not present in workspace. |
