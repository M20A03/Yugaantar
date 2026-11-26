# MediShield — Final Technical Hardening Report

## 1. Before-vs-After Hardening Metrics

| Metric / Test | Before Hardening | After Hardening | Evidence |
|---|---|---|---|
| Handwritten Lowercase PII (`unprefixed_lowercase_names`, 42 cases) | `0.0%` | **100.0%** | `training/final_submission_audit.py` |
| Prepositional & Unfamiliar Lowercase Challenge (15 cases, incl. `Parkinson's`, `Wilson's`, `Dr.`) | Not tested | **P=1.0, R=1.0, F1=1.0, FP=0** | `training/technical_hardening_eval.py` |
| Shared-Family-Phone Linkage (240 adversarial pairs) | Auto-merged FPs | **0 FP, 80 TP, 80 TN, 80 Review** (`auto_F1=1.0`) | `training/technical_hardening_eval.py` |
| Distinct-Patient $k$-Anonymity (`reid_lab(36, 42)`) | Inflated (`record_k=2`) | **Distinct `min_k=1, avg_k=3.27`** | `reid_lab.py` |
| Policy Optimization (`500` patients, 5 / 10 / 20-yr bands) | `5-yr` fixed | **10-yr default: 2.30% forced top-match, avg_k=41.67** | `training/technical_hardening_eval.py` |
| File-to-File CLI Throughput (200 mixed `.txt`/`.json` files) | In-memory only | **927.6 files/sec (`1.08 ms/file`, `188.59 MB` RAM)** | `training/technical_hardening_eval.py` |
| Automated Backend & QA Suite (`pytest -v backend/tests`) | 15 passed | **16/16 passed** | `backend/tests/` |

## 2. Source Files Modified & Created
- **Modified:** `backend/app/services/pii_detection/detector.py` (sliding-window Indian name pair + prepositional/clinical context extraction + `Parkinson's`/`Wilson's`/`marez was admitted` guards)
- **Created:** `backend/app/services/anonymization/release_gate.py` (fail-closed clinical recovery/blocking gate + independent second-pass `independent_privacy_verify`)
- **Modified:** `main.py` & `backend/app/api/routes.py` (wired `release_gate.py` into CLI, `/anonymize`, `/batch-process`; added symlink rejection in `main.py`)
- **Created:** `training/technical_hardening_eval.py` & expanded `backend/tests/test_grand_finale_qa.py`

## 3. Remaining Honest Limitations & Official Status
1. **Unprefixed Lowercase Outside Lexicon & Context:** Completely unfamiliar lowercase names with no prepositional/clinical cue and not in the lightweight lexicon can still be missed.
2. **Synthetic-Only Scope:** Observed `0.0%` direct PII leakage and `100.0%` clinical preservation apply strictly to the evaluated synthetic benchmarks, not all real-world inputs.
3. **Residual Quasi-Identifiers:** Age bands (`10-yr` default) and gender allow forced-guess accuracy $\approx 1/k$ (`2.30%` at $N=500$).
4. **Official Validator:** `validate_output.py` is not present in workspace (**PENDING — ORGANIZER CONFIRMATION REQUIRED**).
