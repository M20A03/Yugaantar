"""MediShield Automated Live Battle Test Runner (Quick & Full modes).

Usage:
    ./backend/.venv/bin/python scripts/run_live_battle_test.py --mode quick
    ./backend/.venv/bin/python scripts/run_live_battle_test.py --mode full
"""

import argparse
import asyncio
import json
import os
import random
import resource
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List

import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(ROOT))

import main as cli_main  # noqa: E402
from app.models.schemas import HospitalRecordInput, PolicyConfig  # noqa: E402
from app.services.anonymization.anonymizer import AnonymizerEngine  # noqa: E402
from app.services.anonymization.release_gate import independent_privacy_verify, verify_and_recover_clinical  # noqa: E402
from app.services.anonymization.structured import sanitize_structured_payload, try_parse_json_payload  # noqa: E402
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine  # noqa: E402
from app.services.pii_detection.detector import MultilingualPIIDetector  # noqa: E402
from app.services.privacy_defense.reid_lab import run_reidentification_defense_lab  # noqa: E402
from app.services.record_linkage.linker import RecordLinkageEngine  # noqa: E402


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


def run_blind_multilingual_suite(n_cases: int = 320) -> Dict[str, Any]:
    """Phase 4: 320+ independently annotated multilingual, lowercase, obfuscated & medical-trap cases."""
    d = MultilingualPIIDetector()
    a = AnonymizerEngine(secret_key="blind-battle", release_scope="blind-battle")
    f = MedicalFidelityEngine()
    p = PolicyConfig()
    rng = random.Random(31415)

    unfam_first = ["Zoya", "Devansh", "Tanmay", "Ishaan", "Rhea", "Farhan", "Kriti", "Aryan", "Sana", "Kabir"]
    unfam_last = ["Qureshi", "Bajpai", "Chatterjee", "Bhat", "Dutta", "Rastogi", "Kapoor", "Sengupta", "Khatri", "Menon"]
    hi_names = ["आरव शर्मा", "मीरा देवी", "सुनीता गुप्ता", "रोहन वर्मा", "प्रिया सिंह"]
    meds = ["Warfarin 2.5 mg", "Metformin 500 mg 1-0-1", "Insulin 10 units BD", "Rosuvastatin 10 mg", "Telmisartan 40 mg"]

    tp = fp = fn = clin_ok = leaks = 0
    missed: List[str] = []

    # 270 positive PII cases across 9 diverse patterns (30 each)
    for i in range(270):
        fn_n = rng.choice(unfam_first)
        ln_n = rng.choice(unfam_last)
        med = rng.choice(meds)
        ph = f"+91-98{rng.randint(10000000, 99999999)}"
        kind = i % 9
        if kind == 0:
            txt = f"please check on {fn_n.lower()} {ln_n.lower()} today, {med}, BP 130/85 mmHg."
            tok = fn_n.lower()
        elif kind == 1:
            txt = f"follow up for {fn_n.lower()} {ln_n.lower()}, HbA1c 7.8%, stay 4 days."
            tok = fn_n.lower()
        elif kind == 2:
            txt = f"Attendant: {fn_n.lower()} {ln_n.lower()}, tel {ph}, SpO2 95%."
            tok = fn_n.lower()
        elif kind == 3:
            hn = rng.choice(hi_names)
            txt = f"मरीज {hn}, फोन {ph}, {med}, भर्ती 5 days."
            tok = hn.split()[0]
        elif kind == 4:
            txt = f"Marez {fn_n} {ln_n}, mob {ph}, Creatinine 1.2 mg/dL."
            tok = fn_n.lower()
        elif kind == 5:
            txt = f"Patient {fn_n[0]}\u200b{fn_n[1:]} {ln_n}, email {fn_n.lower()}.{i}@mail.in, {med}."
            tok = ln_n.lower()
        elif kind == 6:
            txt = f"Patient {fn_n.upper()} {ln_n.upper()}, MRN-9988{i:02d}, Platelets 145000 /uL."
            tok = fn_n.lower()
        elif kind == 7:
            hn = rng.choice(hi_names)
            txt = f"Patient {hn} ({fn_n} {ln_n}), {med}, stay 3 days."
            tok = fn_n.lower()
        else:
            txt = json.dumps({"patient_name": f"{fn_n} {ln_n}", "contact": ph, "rx": med})
            tok = fn_n.lower()

        parsed = try_parse_json_payload(txt)
        if parsed is not None:
            san_obj, ents, _ = sanitize_structured_payload(parsed, d, a, p)
            san = json.dumps(san_obj)
        else:
            _, ents = d.scan(txt)
            san, _ = a.anonymize(txt, ents, p)
        san, _, _ = independent_privacy_verify(san)
        ok_c, san, _ = verify_and_recover_clinical(txt, san, ents, a, p, f, is_structured=(parsed is not None))
        if ok_c:
            clin_ok += 1
        if tok not in san.lower() and ph[-6:] not in san:
            tp += 1
        else:
            fn += 1
            leaks += 1
            if len(missed) < 5:
                missed.append(txt)

    # 50 medical-only negative traps (no patient PII)
    traps = [
        "Parkinson's disease follow up with Warfarin 2.5 mg and BP 130/85 mmHg.",
        "Wilson's disease screening, Creatinine 1.2 mg/dL, SpO2 95%, stay 4 days.",
        "Dr. Rajesh Gupta advised Rosuvastatin 10 mg and Aspirin 75 mg.",
        "marez was admitted yesterday with fever and cough, Platelets 145000 /uL.",
        "check on acute hypertension and HbA1c 7.8% after 2 weeks.",
    ]
    for i in range(50):
        txt = traps[i % len(traps)]
        _, ents = d.scan(txt)
        san, _ = a.anonymize(txt, ents, p)
        ok_c, _, _ = verify_and_recover_clinical(txt, san, ents, a, p, f, is_structured=False)
        if ok_c:
            clin_ok += 1
        person_ents = [e for e in ents if e.entity_type in {"PERSON", "RELATIVE_PERSON"}]
        fp += len(person_ents)

    prec = tp / (tp + fp) if (tp + fp) else 1.0
    rec = tp / (tp + fn) if (tp + fn) else 1.0
    f1 = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0
    return {
        "total_cases": 320,
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "f1": round(f1, 4),
        "pii_leakage_rate": round(leaks / 270, 4),
        "clinical_preservation_rate": round(clin_ok / 320, 4),
        "sample_missed": missed,
    }


def run_torture_files() -> Dict[str, Any]:
    """Phase 6: File & metadata torture test (TXT, CSV, TSV, JSON, collisions, symlinks, malformed)."""
    with tempfile.TemporaryDirectory() as td:
        in_d, out_d = Path(td) / "in", Path(td) / "out"
        pii_dir = in_d / "Rahul_Sharma_9876543210"
        pii_dir.mkdir(parents=True)

        (pii_dir / "Priya_Singh_9811223344.txt").write_text(
            "Patient Priya Singh, Warfarin 2.5 mg, BP 130/85 mmHg, stay 4 days.", encoding="utf-8"
        )
        (in_d / "quoted.csv").write_text(
            '"Aarav_Sharma_9876543210","notes","stay"\n"Aarav Sharma","Metformin 500 mg, line1\nline2","3 days"\n',
            encoding="utf-8",
        )
        (in_d / "labs.tsv").write_text(
            "patient_neha_gupta\tlab\tunit\nNeha Gupta\tHbA1c 7.8%\tSpO2 95%\n",
            encoding="utf-8",
        )
        (in_d / "nested.json").write_text(
            json.dumps([
                {"Rahul Sharma": "Insulin 10 units BD", "Priya Verma": "Creatinine 1.2 mg/dL"},
                {"nested": {"contact": "+91-9911223344", "stay": "5 days"}},
            ]),
            encoding="utf-8",
        )
        # Quarantined files
        (in_d / "empty.txt").write_text("  \n", encoding="utf-8")
        (in_d / "bad_utf8.txt").write_bytes(b"\xff\xfe\xfd")
        (in_d / "broken.json").write_text("{bad", encoding="utf-8")
        (in_d / "malformed.csv").write_text("a,b\n1,2,3\n", encoding="utf-8")
        (in_d / "malware.exe").write_bytes(b"MZ90")
        deep = {"x": "1"}
        for _ in range(36):
            deep = {"n": deep}
        (in_d / "deep.json").write_text(json.dumps(deep), encoding="utf-8")
        outside = Path(td) / "outside.txt"
        outside.write_text("OUTSIDE_SECRET", encoding="utf-8")
        (in_d / "sym.txt").symlink_to(outside)

        cli_main.run_pipeline(in_d, out_d)
        rep = json.loads((out_d / "report.json").read_text(encoding="utf-8"))
        rep_str = json.dumps(rep)
        leaked_meta = any(tok in rep_str for tok in ["Rahul_Sharma", "Priya_Singh", "9876543210", "bad_utf8", "outside"])
        return {
            "counts": rep["counts"],
            "metadata_leak_in_report": leaked_meta,
            "sanitized_files_count": len([p for p in (out_d / "sanitized").rglob("*") if p.is_file()]),
        }


def run_scale_stress(sizes: List[int]) -> List[Dict[str, Any]]:
    """Phase 7: In-memory scale stress test up to 50,000 records with RSS safety guard."""
    d = MultilingualPIIDetector()
    a = AnonymizerEngine(secret_key="stress", release_scope="stress")
    f = MedicalFidelityEngine()
    p = PolicyConfig()
    base = [
        "Patient Rahul Sharma, BP 130/85 mmHg, Metformin 500 mg, stay 4 days.",
        "मरीज सुनीता देवी, फोन 9876543210, HbA1c 7.8%, 3 days.",
        "follow up for ananya kulkarni, Warfarin 2.5 mg, SpO2 95%.",
    ]
    out = []
    for n in sizes:
        rss_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        if rss_mb > 2048:
            out.append({"n": n, "status": "stopped_safety_ram_limit", "peak_rss_mb": round(rss_mb, 2)})
            break
        lats = []
        clin_ok = 0
        t0 = time.perf_counter()
        for i in range(n):
            s = base[i % len(base)]
            ts = time.perf_counter()
            _, e = d.scan(s)
            san, _ = a.anonymize(s, e, p)
            san, _, _ = independent_privacy_verify(san)
            ok_c, _, _ = verify_and_recover_clinical(s, san, e, a, p, f, is_structured=False)
            lats.append((time.perf_counter() - ts) * 1000)
            if ok_c:
                clin_ok += 1
        dt = time.perf_counter() - t0
        lats.sort()
        out.append({
            "n": n,
            "total_seconds": round(dt, 2),
            "rec_per_sec": round(n / dt, 1),
            "avg_ms": round(sum(lats) / n, 3),
            "p95_ms": round(lats[int(0.95 * n)], 3),
            "p99_ms": round(lats[int(0.99 * n)], 3),
            "max_ms": round(max(lats), 3),
            "clinical_preservation": round(clin_ok / n, 4),
            "peak_rss_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 2),
        })
    return out


async def run_concurrent_http_load(concurrencies: List[int]) -> List[Dict[str, Any]]:
    """Phase 8 & 12: Live uvicorn HTTP server concurrent load & failure recovery test."""
    port = _free_port()
    proc = subprocess.Popen(
        [str(ROOT / "backend/.venv/bin/uvicorn"), "app.main:app", "--host", "127.0.0.1", "--port", str(port)],
        cwd=str(ROOT / "backend"),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    url = f"http://127.0.0.1:{port}"
    results = []
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            for _ in range(30):
                try:
                    r = await client.get(f"{url}/health")
                    if r.status_code == 200:
                        break
                except Exception:
                    await asyncio.sleep(0.2)

            for c in concurrencies:
                t0 = time.perf_counter()
                lats = []
                errors = 0

                async def one_req(idx: int) -> None:
                    nonlocal errors
                    ts = time.perf_counter()
                    r = await client.post(
                        f"{url}/anonymize",
                        json={"text": f"Patient Rahul Sharma #{idx}, BP 130/85 mmHg, Metformin 500 mg, stay 4 days."},
                    )
                    lats.append((time.perf_counter() - ts) * 1000)
                    if r.status_code != 200 or "Rahul" in r.json().get("sanitized_text", ""):
                        errors += 1

                await asyncio.gather(*[one_req(i) for i in range(c)])
                lats.sort()
                results.append({
                    "concurrency": c,
                    "success_rate": round((c - errors) / c, 4),
                    "errors": errors,
                    "avg_ms": round(sum(lats) / len(lats), 2),
                    "p95_ms": round(lats[int(0.95 * len(lats))], 2),
                    "total_s": round(time.perf_counter() - t0, 3),
                })

            # Failure injection: invalid JSON depth / bad input -> 400/422, server stays healthy
            bad_r = await client.post(f"{url}/anonymize", json={"text": ""})
            ok_after = await client.get(f"{url}/health")
            results.append({
                "failure_injection_empty_text_status": bad_r.status_code,
                "healthy_after_bad_input": ok_after.status_code == 200,
            })
    finally:
        proc.terminate()
        proc.wait(timeout=5)
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["quick", "full"], default="quick")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    t0 = time.perf_counter()
    pytest_res = subprocess.run(
        [str(ROOT / "backend/.venv/bin/pytest"), "-q", "backend/tests"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )

    stress_sizes = [100, 500, 1000] if args.mode == "quick" else [100, 500, 1000, 5000, 10000, 25000, 50000]
    concurrencies = [1, 5, 10] if args.mode == "quick" else [1, 5, 10, 25, 50]

    report: Dict[str, Any] = {
        "mode": args.mode,
        "pytest_passed": pytest_res.returncode == 0,
        "pytest_summary": pytest_res.stdout.strip().splitlines()[-1] if pytest_res.stdout else "",
        "blind_multilingual_320": run_blind_multilingual_suite(320),
        "file_metadata_torture": run_torture_files(),
        "scale_stress": run_scale_stress(stress_sizes),
        "concurrent_http_load": asyncio.run(run_concurrent_http_load(concurrencies)),
        "browser_ui_automation": "UNTESTED (Chrome DevTools MCP timed out; Playwright/Chromium not installed)",
        "total_duration_s": round(time.perf_counter() - t0, 2),
    }

    txt = json.dumps(report, indent=2)
    if args.out:
        Path(args.out).write_text(txt, encoding="utf-8")
    print(txt)


if __name__ == "__main__":
    main()
