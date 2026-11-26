"""Offline raksha.toml CLI entrypoint for MediShield Track 3 submission.

Usage:
    python main.py --input <input_dir> --output <output_dir>
"""

import argparse
import csv
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent / "backend"))

from app.models.schemas import PolicyConfig  # noqa: E402
from app.services.anonymization.anonymizer import AnonymizerEngine  # noqa: E402
from app.services.pii_detection.detector import MultilingualPIIDetector  # noqa: E402


SUPPORTED_EXTS = {".txt", ".csv", ".tsv", ".json"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def run_pipeline(input_dir: Path, output_dir: Path) -> None:
    t0 = time.perf_counter()
    sanitized_root = output_dir / "sanitized"
    sanitized_root.mkdir(parents=True, exist_ok=True)

    detector = MultilingualPIIDetector()
    anonymizer = AnonymizerEngine()
    policy = PolicyConfig()

    report_files: List[Dict[str, Any]] = []
    records_jsonl_lines: List[str] = []
    counts = {
        "files_total": 0,
        "files_sanitized": 0,
        "files_quarantined": 0,
        "records_processed": 0,
        "identifiers_detected": 0,
        "records_linked": 0,
        "records_generalized": 0,
        "records_suppressed": 0,
        "records_quarantined": 0,
    }

    for src_path in sorted(input_dir.rglob("*")):
        if not src_path.is_file():
            continue
        counts["files_total"] += 1
        rel = src_path.relative_to(input_dir)
        file_hash = sha256_file(src_path)
        ext = src_path.suffix.lower()

        if ext not in SUPPORTED_EXTS:
            counts["files_quarantined"] += 1
            counts["records_quarantined"] += 1
            report_files.append(
                {
                    "input_sha256": file_hash,
                    "output": None,
                    "status": "quarantined",
                    "reason": "unsupported format",
                }
            )
            continue

        try:
            raw_text = src_path.read_text(encoding="utf-8", errors="strict")
        except UnicodeDecodeError:
            counts["files_quarantined"] += 1
            counts["records_quarantined"] += 1
            report_files.append(
                {
                    "input_sha256": file_hash,
                    "output": None,
                    "status": "quarantined",
                    "reason": "invalid encoding",
                }
            )
            continue

        if not raw_text.strip():
            counts["files_quarantined"] += 1
            counts["records_quarantined"] += 1
            report_files.append(
                {
                    "input_sha256": file_hash,
                    "output": None,
                    "status": "quarantined",
                    "reason": "empty file",
                }
            )
            continue

        # Metadata privacy: sanitize directory segments and filename with keyed opaque IDs
        safe_parts: List[str] = []
        for part in rel.parent.parts:
            _, p_ents = detector.scan(part.replace("_", " ").replace("-", " "))
            if p_ents:
                safe_parts.append(anonymizer.opaque_metadata_id("dir", part))
            else:
                safe_parts.append(part)
        safe_parent = Path(*safe_parts) if safe_parts else Path(".")

        _, fn_ents = detector.scan(rel.stem.replace("_", " ").replace("-", " "))
        if fn_ents:
            safe_name = f"{anonymizer.opaque_metadata_id('redacted', rel.name)}{ext}"
        else:
            safe_name = rel.name

        dst_rel = safe_parent / safe_name if str(safe_parent) != "." else Path(safe_name)
        dst_path = sanitized_root / dst_rel
        rel_out = f"sanitized/{dst_rel.as_posix()}"

        if ext in {".csv", ".tsv"}:
            delim = "\t" if ext == ".tsv" else ","
            reader = csv.DictReader(raw_text.splitlines(), delimiter=delim)
            rows = list(reader)
            if (
                not rows
                or not reader.fieldnames
                or any(fn is None for fn in reader.fieldnames)
                or any(None in r for r in rows)
            ):
                counts["files_quarantined"] += 1
                counts["records_quarantined"] += 1
                report_files.append({"input_sha256": file_hash, "output": None, "status": "quarantined", "reason": "malformed or empty table"})
                continue

            raw_fieldnames = list(reader.fieldnames)
            used_headers: set[str] = set()
            header_map: Dict[str, str] = {}
            for fn in raw_fieldnames:
                _, h_ents = detector.scan(fn.replace("_", " ").replace("-", " "))
                if h_ents:
                    base_h = anonymizer.opaque_metadata_id("field", fn)
                else:
                    base_h = fn
                cand = base_h
                suffix = 2
                while cand in used_headers:
                    cand = f"{base_h}_{suffix}"
                    suffix += 1
                used_headers.add(cand)
                header_map[fn] = cand

            dst_path.parent.mkdir(parents=True, exist_ok=True)
            san_fieldnames = [header_map[fn] for fn in raw_fieldnames]
            with dst_path.open("w", encoding="utf-8", newline="") as f_out:
                writer = csv.DictWriter(f_out, fieldnames=san_fieldnames, delimiter=delim)
                writer.writeheader()
                for row_idx, row in enumerate(rows):
                    counts["records_processed"] += 1
                    san_row = {}
                    patient_psn = None
                    for k, v in row.items():
                        val = v or ""
                        _, ents = detector.scan(val)
                        counts["identifiers_detected"] += len(ents)
                        san_val, _ = anonymizer.anonymize(val, ents, policy)
                        for e in ents:
                            if e.entity_type == "PERSON" and patient_psn is None:
                                patient_psn = anonymizer.pseudonym_for("PERSON", e.text).strip("[]")
                        san_row[header_map[k]] = san_val
                    writer.writerow(san_row)
                    records_jsonl_lines.append(
                        json.dumps({"file": rel_out, "loc": f"row:{row_idx}", "patient": patient_psn})
                    )
        elif ext == ".json":
            try:
                obj = json.loads(raw_text)
            except json.JSONDecodeError:
                counts["files_quarantined"] += 1
                counts["records_quarantined"] += 1
                report_files.append({"input_sha256": file_hash, "output": None, "status": "quarantined", "reason": "invalid json"})
                continue

            if not isinstance(obj, (dict, list)) or len(obj) == 0:
                counts["files_quarantined"] += 1
                counts["records_quarantined"] += 1
                report_files.append({"input_sha256": file_hash, "output": None, "status": "quarantined", "reason": "empty or unsupported json"})
                continue

            def _clean_key(key: str, used: set[str]) -> str:
                _, k_ents = detector.scan(key.replace("_", " ").replace("-", " "))
                if k_ents:
                    base_k = anonymizer.opaque_metadata_id("key", key)
                else:
                    base_k = key
                cand = base_k
                suffix = 2
                while cand in used:
                    cand = f"{base_k}_{suffix}"
                    suffix += 1
                used.add(cand)
                return cand

            def _clean(x: Any) -> Any:
                if isinstance(x, str):
                    _, e_list = detector.scan(x)
                    counts["identifiers_detected"] += len(e_list)
                    s_val, _ = anonymizer.anonymize(x, e_list, policy)
                    return s_val
                if isinstance(x, list):
                    return [_clean(i) for i in x]
                if isinstance(x, dict):
                    used_keys: set[str] = set()
                    return {_clean_key(str(k), used_keys): _clean(v) for k, v in x.items()}
                return x

            cleaned_obj = _clean(obj)
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            dst_path.write_text(json.dumps(cleaned_obj, ensure_ascii=False, indent=2), encoding="utf-8")

            if isinstance(obj, list):
                for idx, item in enumerate(obj):
                    counts["records_processed"] += 1
                    _, item_ents = detector.scan(json.dumps(item, ensure_ascii=False))
                    psn = next((anonymizer.pseudonym_for("PERSON", e.text).strip("[]") for e in item_ents if e.entity_type == "PERSON"), None)
                    records_jsonl_lines.append(json.dumps({"file": rel_out, "loc": f"/{idx}", "patient": psn}))
            else:
                counts["records_processed"] += 1
                _, ents = detector.scan(raw_text)
                psn = next((anonymizer.pseudonym_for("PERSON", e.text).strip("[]") for e in ents if e.entity_type == "PERSON"), None)
                records_jsonl_lines.append(json.dumps({"file": rel_out, "loc": "/", "patient": psn}))
        else:
            lines = [ln for ln in raw_text.splitlines() if ln.strip()]
            san_lines: List[str] = []
            for idx, line in enumerate(lines):
                counts["records_processed"] += 1
                _, ents = detector.scan(line)
                counts["identifiers_detected"] += len(ents)
                san_txt, _ = anonymizer.anonymize(line, ents, policy)
                san_lines.append(san_txt)
                psn = next((anonymizer.pseudonym_for("PERSON", e.text).strip("[]") for e in ents if e.entity_type == "PERSON"), None)
                records_jsonl_lines.append(json.dumps({"file": rel_out, "loc": f"line:{idx}" if len(lines) > 1 else "doc", "patient": psn}))
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            dst_path.write_text("\n".join(san_lines) + ("\n" if san_lines else ""), encoding="utf-8")

        counts["files_sanitized"] += 1
        report_files.append({"input_sha256": file_hash, "output": rel_out, "status": "sanitized"})

    report = {
        "files": report_files,
        "counts": counts,
        "timing": {"seconds": round(time.perf_counter() - t0, 3)},
    }
    (output_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (output_dir / "records.jsonl").write_text("\n".join(records_jsonl_lines) + ("\n" if records_jsonl_lines else ""), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MediShield Offline Privacy Firewall CLI")
    parser.add_argument("--input", required=True, help="Input directory")
    parser.add_argument("--output", required=True, help="Output directory")
    args = parser.parse_args()
    run_pipeline(Path(args.input), Path(args.output))
