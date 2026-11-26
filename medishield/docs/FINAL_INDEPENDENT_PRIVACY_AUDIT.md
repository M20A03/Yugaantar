# MediShield — Final Independent Privacy Engineering Audit

**Audit Scope:** Independent, skeptical evaluation of MediShield Healthcare Privacy Firewall (Track 3: Secret Wards) across large-scale cohorts (100–5,000 synthetic patients), attacker modeling, adaptive $k$-anonymity, metadata security, 5,000-example clinical integrity, 1,400-example multilingual PII stress testing, and CPU/RAM performance.

**Frozen Model Integrity:** No frozen `.joblib` artifacts in `medishield/backend/artifacts/` were modified or retrained.

---

## 1. Critique of Earlier 0% Re-Identification Claim (`reid_lab.py`)

Earlier testing reported **0% re-identification after sanitization** on 36 synthetic patients. Our independent audit found that this result **overstated robustness** for three reasons:
1. **Unitary Confidence Check Only:** `reid_lab.py` only counted a re-identification hit when `voter_bucket_counts[(age_bucket, gender)] == 1`. Whenever $\ge 2$ voters shared an age bucket and gender, the simulated attacker made **zero guesses**, understating **forced top-match accuracy** ($\mathbb{E}[1/|C|]$).
2. **Narrow Leakage Checks:** `reid_lab.py` checked only `first_name` and `phone[-6:]`, missing last-name, PIN-code, and unredacted city/location leakage.
3. **Template Overlap:** The initial cohort used fixed prefixes (`Patient`, `Mariz`, `मरीज़`) that matched 100% of `detector.py`'s existing rules, masking real-world spelling and phrasing gaps.

---

## 2. Dataset Independence Verification

All audit runs used `medishield/training/independent_privacy_audit.py` with:
- Disjoint synthetic name, city, PIN, medication, and template pools (`Hosp_Alpha`, `Hosp_Beta`, `Hosp_Gamma`, `Hosp_Delta`).
- Spelling variants (`Marez`, `मरीज` without nukta), unstructured clinical prose (`<Name> was admitted`), parenthetical demographics (`<Name> (45/M)`), `City:` / `शहर` / `from <City> <PIN>`, and `Attendant:` prefixes.
- Strict separation: initial failure discovery was treated as development/regression data, and final post-fix verification was run on a **fresh sealed seed (`99999 + N`)**.

---

## 3. Large-Scale Privacy Resistance by Cohort Size (Before vs. After Fix)

### A. Pre-Fix Audit (Exposed Real Gaps)
| Cohort (Patients / Records / Voters) | Direct PII Leakage | Unique Re-ID Rate | Forced Top-Match Accuracy | Min / Avg Group Size |
|---|---|---|---|---|
| 100 / 246 / 150 | 76.02% | 47.97% | 58.08% | 1 / 15.61 |
| 500 / 1,256 / 750 | 73.41% | 42.68% | 48.99% | 1 / 37.70 |
| 1,000 / 2,507 / 1,500 | 74.47% | 35.86% | 43.79% | 1 / 81.03 |
| 5,000 / 12,499 / 7,500 | 75.17% | 17.28% | 28.71% | 1 / 376.90 |

**Root Causes Found:**
- `detector.py` missed `Marez`, `मरीज` (no nukta), `Attendant:`, `<Name> was admitted`, and `from <City>` / `City:` / `शहर`.
- Once city, PIN, or name leaked, the attacker narrowed the voter list down to $k=1$ on up to 47.97% of records.

### B. Post-Fix Audit on Fresh Sealed Cohorts (`seed = 99999 + N`)
After surgical, generalizable updates to `detector.py` (multilingual context & location cues):

| Cohort (Patients / Records / Voters) | Direct PII Leakage | Unique Re-ID Rate | Incorrect Confident Rate | Attacker Coverage | Forced Top-Match Accuracy | Min / Median / Avg Group Size | Residual QI Exposure | Cross-Record Unique Rate |
|---|---|---|---|---|---|---|---|---|
| 100 / 248 / 150 | **0.0%** | **0.0%** | 0.0% | 100% | **11.14%** | 2 / 9 / 26.93 | 100% | 0.0% (84 pseudonyms) |
| 500 / 1,280 / 750 | **0.0%** | **0.0%** | 0.0% | 100% | **2.36%** | 4 / 38 / 136.78 | 100% | 0.0% (44 pseudonyms) |
| 1,000 / 2,485 / 1,500 | **0.0%** | **0.0%** | 0.0% | 100% | **1.19%** | 5 / 70 / 262.68 | 100% | 0.0% (17 pseudonyms) |
| 5,000 / 12,529 / 7,500 | **0.0%** | **0.0%** | 0.0% | 100% | **0.24%** | 55 / 305 / 1,316.27 | 100% | 0.0% |

**Why Forced Top-Match Accuracy is Non-Zero (11.14% -> 0.24%):**
Even with 0% direct PII leakage, 5-year age bands (`40–44`) and gender (`M`/`F`) remain in the sanitized output (`residual_qi_exposure_rate = 1.0`). When forced to pick randomly from an equivalence class of average size $k$, the attacker succeeds at rate $\approx 1/k$ (11.14% at $N=100$, dropping to 0.24% at $N=5,000$).

---

## 4. Adaptive Anonymization ($k$-Anonymity / Age-Band Trade-Off on 500 Patients)

Measured on the 500-patient cohort (pre-fix baseline, showing the structural effect of `age_band_size`):
| Age Band Size | Unique Re-ID Rate | Forced Top-Match Accuracy | Median Group Size | Clinical Preservation |
|---|---|---|---|---|
| 2 years | 47.13% | 54.53% | 2 | **100.0%** |
| 5 years | 42.42% | 48.85% | 3 | **100.0%** |
| 10 years | 37.24% | 44.77% | 6 | **100.0%** |
| 20 years | 30.30% | 39.87% | 7 | **100.0%** |

**Key Limitation:** $k$-anonymity reduces uniqueness as groups grow, **never guarantees** zero re-identification (e.g., against attribute disclosure or external background knowledge), and cannot compensate for direct PII leakage. Protected medications, dosages, labs, vitals, and stay lengths are never altered.

---

## 5. Metadata Security Audit Findings (`main.py` & `anonymizer.py`)

**Pre-Fix Vulnerability Found:**
- `medishield/main.py` previously used **unkeyed** `hashlib.sha256(...)[:8]` for `dir_`, `redacted_`, `field_`, and `key_`. Unkeyed hashes allow dictionary precomputation on common column names (`patient_name`, `phone`) and cross-release correlation.

**Remediation Applied:**
- Added `AnonymizerEngine.opaque_metadata_id(kind, value)` in `anonymizer.py` using **keyed HMAC-SHA256** derived from `RAKSHA_SECRET` and `release_scope` (no custom cryptography).
- Updated `main.py` to replace all PII-bearing directories, filenames, CSV/TSV headers, and JSON keys with release-scoped keyed opaque tokens (`dir_<hmac10>`, `redacted_<hmac10>`, `field_<hmac10>`, `key_<hmac10>`) with collision suffixes (`_2`, `_3`) so clinical values are never overwritten.
- Quarantined files (corrupted UTF-8, empty files, invalid/empty JSON, unsupported formats, malformed CSV rows) are recorded only by `input_sha256` and never exposed by original filename or copied to `sanitized/`.

---

## 6. Clinical Integrity Stress Test (5,000 Diverse Examples)

| Clinical Category | Total Tested | Preserved | Preservation Rate |
|---|---|---|---|
| Medication names (incl. non-whitelist drugs) | 5,000 | 5,000 | **100.0%** |
| Decimal dosages (`12.5 mg`, `0.25 mg`, `7.5 ml`) | 5,000 | 5,000 | **100.0%** |
| Multiple dosage units (`mg`, `ml`, `units`, `IU`, `puffs`) | 5,000 | 5,000 | **100.0%** |
| Medication frequencies (`1-0-1`, `BD`, `OD`, `TDS`, `QID`, `HS`, `SOS`, `q8h`) | 5,000 | 5,000 | **100.0%** |
| Lab measurements & units (`HbA1c 8.1%`, `TSH 4.6 mIU/L`, `Platelets 145000 /uL`) | 5,000 | 5,000 | **100.0%** |
| Vital measurements (`BP 138/88 mmHg`, `HR 88 bpm`, `SpO2 95%`, `RR 18 /min`) | 5,000 | 5,000 | **100.0%** |
| Hospital stay lengths (`2 days`, `12 days`, `2 weeks`) | 5,000 | 5,000 | **100.0%** |
| Medical abbreviations (`T2DM`, `HTN`, `CAD`, `CKD`, `COPD`, `AKI`) | 5,000 | 5,000 | **100.0%** |
| Clinical numbers resembling IDs (`145000`, `11200`, `981234`, `2026112601`) | 5,000 | 5,000 | **100.0%** |

**Evaluator Audit Limitation:** `MedicalFidelityEngine` (`fidelity.py`) uses a closed regex list of common Indian clinical terms rather than a full UMLS/SNOMED ontology, so it only scores the clinical terms in its pattern list. Independent ground-truth checking confirms 100.0% preservation on all 5,000 examples.

---

## 7. Multilingual PII Stress Test (1,400 Adversarial Examples)

| Adversarial Pattern (200 cases each) | Pre-Fix Name Recall | Post-Fix Name Recall | Phone Recall |
|---|---|---|---|
| `spelling_mariz` (`Mariz <Name>`) | 100.0% | **100.0%** | 100.0% |
| `spelling_marez` (`Marez <Name>`) | **0.0%** | **100.0%** | 100.0% |
| `spelling_pateint` (`Pateint <Name>`) | 100.0% | **100.0%** | 100.0% |
| `unstructured_admitted` (`<Name> was admitted`) | **0.0%** | **100.0%** | 100.0% |
| `attendant_ctx` (`Attendant: <Name>`) | **0.0%** | **100.0%** | 100.0% |
| `hindi_no_nukta` (`मरीज <Name>`) | **0.0%** | **100.0%** | 100.0% |
| `zero_width_obfuscation` (`R\u200bahul`) | 100.0% | **100.0%** | 100.0% |

---

## 8. Performance, Offline & Test Verification

- **Offline / CPU-only:** Verified; zero network calls, zero LLMs.
- **Model loading time:** `97.42 ms`
- **Peak process RSS RAM:** `199.36 MB`
- **Throughput & Latency (sealed cohorts):**
  - 100 patients (248 records): `2,292.9 rec/sec`, avg `0.39 ms`, P95 `0.82 ms`
  - 5,000 patients (12,529 records): `429.7 rec/sec`, avg `0.51 ms`, P95 `0.99 ms`
- **Automated Tests:** `pytest -v backend/tests` -> **10/10 passed**.
- **Official Validator:** Not present in workspace (`Requires official clarification` per `HACKATHON_COMPLIANCE_MATRIX.md`).

---

## 9. Remaining Limitations (For Technical Viva)

1. **Unprefixed / Lowercase Names:** If a person's name appears completely lowercase in an unstructured English sentence without any context word (`"met rahul sharma yesterday"`), rule-based + char TF-IDF detection can still miss it.
2. **Residual Quasi-Identifiers:** Age bands and gender allow forced-guess accuracy of `1/k` (~11.1% in tiny 100-patient cohorts, ~0.24% in 5,000-patient cohorts).
3. **Closed Clinical Dictionary in `fidelity.py`:** `MedicalFidelityEngine` checks a curated regex set; unseen rare drugs are preserved by `anonymizer.py` but not explicitly scored by `fidelity.py`.
4. **No Official Organizer `validate_output.py`:** Exact CLI output schema compatibility awaits official organizer release.
