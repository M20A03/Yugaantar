"""Offline raksha.toml CLI entrypoint for MediShield Track 3 submission.

Usage:
    python main.py --input <input_dir> --output <output_dir>
"""

import argparse
import csv
import hashlib
import json
import os
import resource
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent / "backend"))

from app.models.schemas import PolicyConfig  # noqa: E402
from app.services.anonymization.anonymizer import AnonymizerEngine  # noqa: E402
from app.services.anonymization.release_gate import (  # noqa: E402
    independent_privacy_verify,
    verify_and_recover_clinical,
)
from app.services.anonymization.structured import (  # noqa: E402
    StructuredDepthError,
    sanitize_structured_payload,
)
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine  # noqa: E402
from app.services.pii_detection.detector import MultilingualPIIDetector  # noqa: E402


SUPPORTED_EXTS = {".txt", ".csv", ".tsv", ".json"}
MAX_FILE_BYTES = 10 * 1024 * 1024


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
    fidelity = MedicalFidelityEngine()
    policy = PolicyConfig()

    report_files: List[Dict[str, Any]] = []
    records_jsonl_lines: List[str] = []
    counts = {
        "files_total": 0,
        "files_sanitized": 0,
        "files_quarantined": 0,
        "clinical_integrity_flagged": 0,
        "records_processed": 0,
        "identifiers_detected": 0,
        "records_linked": 0,
        "records_generalized": 0,
        "records_suppressed": 0,
        "records_quarantined": 0,
    }

    for src_path in sorted(input_dir.rglob("*")):
        if src_path.is_symlink():
            counts["files_total"] += 1
            counts["files_quarantined"] += 1
            counts["records_quarantined"] += 1
            report_files.append(
                {
                    "input_sha256": None,
                    "output": None,
                    "status": "quarantined",
                    "reason": "symlink rejected",
                }
            )
            continue
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

        if src_path.stat().st_size > MAX_FILE_BYTES:
            counts["files_quarantined"] += 1
            counts["records_quarantined"] += 1
            report_files.append(
                {
                    "input_sha256": file_hash,
                    "output": None,
                    "status": "quarantined",
                    "reason": "file exceeds size limit",
                }
            )
            continue

        try:
            raw_bytes = src_path.read_bytes()
            if raw_bytes.startswith((b"\xff\xfe", b"\xfe\xff")) and len(raw_bytes) >= 8:
                raw_text = raw_bytes.decode("utf-16", errors="strict")
            elif raw_bytes.startswith(b"\xef\xbb\xbf"):
                raw_text = raw_bytes[3:].decode("utf-8", errors="strict")
            else:
                raw_text = raw_bytes.decode("utf-8", errors="strict")
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

            import io as _io
            buf = _io.StringIO()
            san_fieldnames = [header_map[fn] for fn in raw_fieldnames]
            writer = csv.DictWriter(buf, fieldnames=san_fieldnames, delimiter=delim)
            writer.writeheader()
            file_records_jsonl: List[str] = []
            for row_idx, row in enumerate(rows):
                counts["records_processed"] += 1
                san_row = {}
                patient_psn = None
                # Combine FirstName + LastName if present for consistent patient pseudonym
                fn_cell = (row.get("FirstName") or row.get("first_name") or "").strip()
                ln_cell = (row.get("LastName") or row.get("last_name") or "").strip()
                combined_name = f"{fn_cell} {ln_cell}".strip()
                if combined_name:
                    patient_psn = anonymizer.pseudonym_for("PERSON", combined_name).strip("[]")

                for k, v in row.items():
                    val = v or ""
                    kl = (k or "").strip().lower()
                    if not val.strip():
                        san_row[header_map[k]] = val
                        continue
                    if any(t in kl for t in ("patientid", "uhid", "mrn", "reg no", "reg_no", "insurance")):
                        counts["identifiers_detected"] += 1
                        san_row[header_map[k]] = "[ID_REDACTED]"
                    elif any(t in kl for t in ("firstname", "lastname", "patient name", "patient_name", "naam", "guardian", "relative name", "pita", "pati")):
                        counts["identifiers_detected"] += 1
                        san_row[header_map[k]] = anonymizer.pseudonym_for("PERSON", val)
                        if patient_psn is None and "guardian" not in kl and "relative" not in kl and "pita" not in kl:
                            patient_psn = anonymizer.pseudonym_for("PERSON", val).strip("[]")
                    elif any(t in kl for t in ("dob", "janm", "birth")):
                        counts["identifiers_detected"] += 1
                        san_row[header_map[k]] = "[DOB_REDACTED]"
                    elif any(t in kl for t in ("age", "umar")) and val.strip().isdigit():
                        age_v = int(val.strip())
                        lo = (age_v // policy.age_band_size) * policy.age_band_size
                        san_row[header_map[k]] = f"{lo}-{lo + policy.age_band_size - 1}"
                        counts["records_generalized"] += 1
                    elif any(t in kl for t in ("street", "city", "district", "zip", "address", "pata", "gaon", "tehsil", "jila", "pin", "village", "mohalla", "locality", "landmark", "house")):
                        counts["identifiers_detected"] += 1
                        san_row[header_map[k]] = "[LOCATION_REDACTED]"
                    elif any(t in kl for t in ("phone", "mobile", "email", "aadhaar", "aadhar", "abha", "pan")):
                        counts["identifiers_detected"] += 1
                        san_row[header_map[k]] = "[REDACTED]"
                    else:
                        _, ents = detector.scan(val)
                        counts["identifiers_detected"] += len(ents)
                        san_val, _ = anonymizer.anonymize(val, ents, policy)
                        for e in ents:
                            if e.entity_type == "PERSON" and patient_psn is None:
                                patient_psn = anonymizer.pseudonym_for("PERSON", e.text).strip("[]")
                        san_row[header_map[k]] = san_val
                writer.writerow(san_row)
                file_records_jsonl.append(
                    json.dumps({"file": rel_out, "loc": f"row:{row_idx}", "patient": patient_psn})
                )
            sanitized_out_text = buf.getvalue()
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

            try:
                cleaned_obj, j_ents, _ = sanitize_structured_payload(obj, detector, anonymizer, policy)
            except StructuredDepthError:
                counts["files_quarantined"] += 1
                counts["records_quarantined"] += 1
                report_files.append({"input_sha256": file_hash, "output": None, "status": "quarantined", "reason": "json nesting too deep"})
                continue

            counts["identifiers_detected"] += len(j_ents)
            sanitized_out_text = json.dumps(cleaned_obj, ensure_ascii=False, indent=2)
            file_records_jsonl = []
            if isinstance(obj, list):
                for idx, item in enumerate(obj):
                    counts["records_processed"] += 1
                    _, item_ents = detector.scan(json.dumps(item, ensure_ascii=False))
                    psn = next((anonymizer.pseudonym_for("PERSON", e.text).strip("[]") for e in item_ents if e.entity_type == "PERSON"), None)
                    file_records_jsonl.append(json.dumps({"file": rel_out, "loc": f"/{idx}", "patient": psn}))
            else:
                counts["records_processed"] += 1
                _, ents = detector.scan(raw_text)
                psn = next((anonymizer.pseudonym_for("PERSON", e.text).strip("[]") for e in ents if e.entity_type == "PERSON"), None)
                file_records_jsonl.append(json.dumps({"file": rel_out, "loc": "/", "patient": psn}))
        else:
            lines = [ln for ln in raw_text.splitlines() if ln.strip()]
            san_lines: List[str] = []
            file_records_jsonl = []
            for idx, line in enumerate(lines):
                counts["records_processed"] += 1
                _, ents = detector.scan(line)
                counts["identifiers_detected"] += len(ents)
                san_txt, _ = anonymizer.anonymize(line, ents, policy)
                san_lines.append(san_txt)
                psn = next((anonymizer.pseudonym_for("PERSON", e.text).strip("[]") for e in ents if e.entity_type == "PERSON"), None)
                file_records_jsonl.append(json.dumps({"file": rel_out, "loc": f"line:{idx}" if len(lines) > 1 else "doc", "patient": psn}))
            sanitized_out_text = "\n".join(san_lines) + ("\n" if san_lines else "")

        # Independent second-pass output privacy verification
        sanitized_out_text, priv_interventions, _ = independent_privacy_verify(sanitized_out_text)
        counts["identifiers_detected"] += priv_interventions

        # Fail-closed clinical integrity gate: verify, attempt safe recovery, or withhold
        clin_ok, sanitized_out_text, fid_res = verify_and_recover_clinical(
            raw_text,
            sanitized_out_text,
            [],
            anonymizer,
            policy,
            fidelity,
            is_structured=(ext != ".txt"),
        )
        if not clin_ok and ext == ".txt":
            repaired_lines: List[str] = []
            lost_vals = {item["value"].lower() for item in fid_res["lost_items"]}
            for line in [ln for ln in raw_text.splitlines() if ln.strip()]:
                _, ents = detector.scan(line)
                safe_ents = [e for e in ents if e.text.lower() not in lost_vals]
                san_txt, _ = anonymizer.anonymize(line, safe_ents, policy)
                san_txt, _, _ = independent_privacy_verify(san_txt)
                repaired_lines.append(san_txt)
            candidate_text = "\n".join(repaired_lines) + ("\n" if repaired_lines else "")
            fid_retry = fidelity.evaluate(raw_text, candidate_text)
            if fid_retry["preservation_score"] >= 1.0:
                sanitized_out_text = candidate_text
                fid_res = fid_retry
                clin_ok = True

        if not clin_ok:
            counts["files_quarantined"] += 1
            counts["records_quarantined"] += 1
            counts["clinical_integrity_flagged"] += 1
            report_files.append(
                {
                    "input_sha256": file_hash,
                    "output": None,
                    "status": "quarantined",
                    "reason": "clinical integrity verification failed",
                    "clinical_preservation": fid_res["preservation_score"],
                }
            )
            continue

        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_path.write_text(sanitized_out_text, encoding="utf-8")
        records_jsonl_lines.extend(file_records_jsonl)
        counts["files_sanitized"] += 1
        report_files.append({"input_sha256": file_hash, "output": rel_out, "status": "sanitized", "clinical_preservation": fid_res["preservation_score"]})

    counts["output_completeness"] = round(
        counts["files_sanitized"] / counts["files_total"], 4
    ) if counts["files_total"] else 1.0

    report = {
        "files": report_files,
        "counts": counts,
        "timing": {"seconds": round(time.perf_counter() - t0, 3)},
        "resources": {
            "peak_rss_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 2)
        },
    }
    (output_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (output_dir / "records.jsonl").write_text("\n".join(records_jsonl_lines) + ("\n" if records_jsonl_lines else ""), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MediShield Offline Privacy Firewall CLI")
    parser.add_argument("--input", required=True, help="Input directory")
    parser.add_argument("--output", required=True, help="Output directory")
    args = parser.parse_args()
    run_pipeline(Path(args.input), Path(args.output))
