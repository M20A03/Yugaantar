"""FastAPI routes for MediShield Healthcare Privacy Firewall."""

import csv
import io
import json
import time
from collections import Counter
from typing import Any, Dict, List

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.models.schemas import (
    AnonymizeRequest,
    AnonymizeResponse,
    BatchProcessResponse,
    FidelityRequest,
    FidelityResponse,
    LinkageRequest,
    LinkageResponse,
    MetricsResponse,
    PolicyConfig,
    QuasiRecord,
    RiskAnalyzeRequest,
    RiskAnalyzeResponse,
    ScanRequest,
    ScanResponse,
)
from app.services.anonymization.anonymizer import AnonymizerEngine
from app.services.evaluation.evaluator import run_evaluation_suite
from app.services.medical_fidelity.fidelity import MedicalFidelityEngine
from app.services.pii_detection.detector import MultilingualPIIDetector
from app.services.privacy_defense.reid_lab import run_reidentification_defense_lab
from app.services.record_linkage.linker import RecordLinkageEngine
from app.services.risk_analysis.risk_analyzer import RiskAnalyzer
from app.services.storage.audit_db import AuditStore


router = APIRouter()

detector = MultilingualPIIDetector()
anonymizer = AnonymizerEngine()
linker = RecordLinkageEngine()
risk_analyzer = RiskAnalyzer()
fidelity_engine = MedicalFidelityEngine()
audit_store = AuditStore()

MAX_UPLOAD_BYTES = 10 * 1024 * 1024  # 10 MB


@router.get("/health")
def health() -> Dict[str, Any]:
    return {
        "status": "ready",
        "service": "MediShield Privacy Firewall",
        "offline_mode": True,
        "llm_usage": False,
    }


@router.post("/scan", response_model=ScanResponse)
def scan_record(req: ScanRequest) -> ScanResponse:
    t0 = time.perf_counter()
    language, entities = detector.scan(req.text)
    counts = dict(Counter(e.entity_type for e in entities))
    dt = (time.perf_counter() - t0) * 1000.0
    audit_store.log_event(
        operation="scan",
        language=language,
        records_count=1,
        entities_detected=len(entities),
        entities_removed=0,
        latency_ms=dt,
        category_counts=counts,
    )
    return ScanResponse(
        language=language,
        entities=entities,
        entity_counts=counts,
        latency_ms=round(dt, 2),
    )


@router.post("/anonymize", response_model=AnonymizeResponse)
def anonymize_record(req: AnonymizeRequest) -> AnonymizeResponse:
    t0 = time.perf_counter()
    language, entities = detector.scan(req.text)
    sanitized, applied = anonymizer.anonymize(req.text, entities, req.policy)
    r_before, r_after = risk_analyzer.score_single_text(entities)
    fid = fidelity_engine.evaluate(req.text, sanitized)
    dt = (time.perf_counter() - t0) * 1000.0

    counts = dict(Counter(e.entity_type for e in entities))
    audit_store.log_event(
        operation="anonymize",
        language=language,
        records_count=1,
        entities_detected=len(entities),
        entities_removed=applied,
        fidelity_score=fid["preservation_score"],
        risk_before=r_before["reidentification_risk_score"],
        risk_after=r_after["reidentification_risk_score"],
        latency_ms=dt,
        category_counts=counts,
    )
    return AnonymizeResponse(
        language=language,
        original_length=len(req.text),
        sanitized_text=sanitized,
        entities=entities,
        transformations_applied=applied,
        risk_before=r_before,
        risk_after=r_after,
        fidelity=fid,
        latency_ms=round(dt, 2),
    )


@router.post("/linkage/analyze", response_model=LinkageResponse)
def analyze_linkage(req: LinkageRequest) -> LinkageResponse:
    t0 = time.perf_counter()
    evaluated, pairs, clusters = linker.analyze(req.records, threshold=req.threshold)
    dt = (time.perf_counter() - t0) * 1000.0
    audit_store.log_event(
        operation="linkage",
        language="multi",
        records_count=len(req.records),
        entities_detected=0,
        entities_removed=0,
        linkage_flagged=len(pairs),
        latency_ms=dt,
    )
    return LinkageResponse(
        total_records=len(req.records),
        candidate_pairs_evaluated=evaluated,
        flagged_pairs=pairs,
        clusters=clusters,
        latency_ms=round(dt, 2),
    )


@router.post("/risk/analyze", response_model=RiskAnalyzeResponse)
def analyze_risk(req: RiskAnalyzeRequest) -> RiskAnalyzeResponse:
    t0 = time.perf_counter()
    before, after, suggestions = risk_analyzer.analyze_batch(
        req.records,
        generalize_age=req.generalize_age,
        generalize_location=req.generalize_location,
        suppress_rare=req.suppress_rare,
        rare_threshold=req.rare_threshold,
    )
    dt = (time.perf_counter() - t0) * 1000.0
    audit_store.log_event(
        operation="risk_analysis",
        language="multi",
        records_count=len(req.records),
        entities_detected=0,
        entities_removed=0,
        risk_before=before["reidentification_risk_score"],
        risk_after=after["reidentification_risk_score"],
        latency_ms=dt,
    )
    return RiskAnalyzeResponse(
        risk_before=before,
        risk_after=after,
        suggestions=suggestions,
        disclaimer=risk_analyzer.DISCLAIMER,
        latency_ms=round(dt, 2),
    )


@router.post("/fidelity/evaluate", response_model=FidelityResponse)
def evaluate_fidelity(req: FidelityRequest) -> FidelityResponse:
    t0 = time.perf_counter()
    res = fidelity_engine.evaluate(req.original_text, req.sanitized_text)
    dt = (time.perf_counter() - t0) * 1000.0
    return FidelityResponse(**res, latency_ms=round(dt, 2))


@router.post("/batch-process", response_model=BatchProcessResponse)
async def batch_process(file: UploadFile = File(...)) -> BatchProcessResponse:
    t0 = time.perf_counter()
    raw = await file.read()
    if len(raw) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="File exceeds 10 MB limit.")
    if not raw:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    filename = file.filename or "records.txt"
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else "txt"
    if ext not in {"csv", "json", "txt"}:
        raise HTTPException(status_code=400, detail="Unsupported format. Use CSV, JSON, or TXT.")

    text_content = raw.decode("utf-8", errors="replace")
    policy = PolicyConfig()
    total_entities = 0
    total_removed = 0
    fidelity_scores: List[float] = []
    preview_rows: List[Dict[str, Any]] = []
    quasi_rows: List[QuasiRecord] = []
    cat_counts: Counter = Counter()

    if ext == "txt":
        lines = [ln for ln in text_content.splitlines() if ln.strip()]
        sanitized_lines: List[str] = []
        for idx, line in enumerate(lines):
            _, ents = detector.scan(line)
            san, rem = anonymizer.anonymize(line, ents, policy)
            fid = fidelity_engine.evaluate(line, san)
            sanitized_lines.append(san)
            total_entities += len(ents)
            total_removed += rem
            fidelity_scores.append(fid["preservation_score"])
            for e in ents:
                cat_counts[e.entity_type] += 1
            if idx < 10:
                preview_rows.append({"row": idx, "sanitized": san, "entities_removed": rem, "fidelity": fid["preservation_score"]})
        sanitized_out = "\n".join(sanitized_lines)
        records_count = len(lines)

    elif ext == "csv":
        reader = csv.DictReader(io.StringIO(text_content))
        if not reader.fieldnames:
            raise HTTPException(status_code=400, detail="CSV missing header row.")
        out_buf = io.StringIO()
        writer = csv.DictWriter(out_buf, fieldnames=reader.fieldnames)
        writer.writeheader()
        records_count = 0
        for idx, row in enumerate(reader):
            records_count += 1
            san_row: Dict[str, Any] = {}
            row_removed = 0
            for k, v in row.items():
                val = v or ""
                if k and any(tok in k.lower() for tok in ("name", "patient", "phone", "mobile", "address", "aadhaar", "pan")):
                    if val.strip():
                        san_val = anonymizer.pseudonym_for(k.upper(), val) if "name" in k.lower() else "[REDACTED]"
                        san_row[k] = san_val
                        total_entities += 1
                        total_removed += 1
                        row_removed += 1
                        cat_counts[k.upper()] += 1
                        continue
                _, ents = detector.scan(val)
                san_val, rem = anonymizer.anonymize(val, ents, policy)
                fid = fidelity_engine.evaluate(val, san_val)
                fidelity_scores.append(fid["preservation_score"])
                total_entities += len(ents)
                total_removed += rem
                row_removed += rem
                for e in ents:
                    cat_counts[e.entity_type] += 1
                san_row[k] = san_val
            writer.writerow(san_row)
            quasi_rows.append(
                QuasiRecord(
                    age=int(row["age"]) if row.get("age", "").isdigit() else None,
                    gender=row.get("gender"),
                    location=row.get("address") or row.get("location"),
                    diagnosis=row.get("diagnosis"),
                )
            )
            if idx < 10:
                preview_rows.append({**san_row, "_entities_removed": row_removed})
        sanitized_out = out_buf.getvalue()

    else:  # json
        try:
            payload = json.loads(text_content)
        except json.JSONDecodeError as exc:
            raise HTTPException(status_code=400, detail=f"Invalid JSON: {exc}") from exc

        def _sanitize_obj(obj: Any) -> Any:
            nonlocal total_entities, total_removed
            if isinstance(obj, str):
                _, ents = detector.scan(obj)
                san, rem = anonymizer.anonymize(obj, ents, policy)
                fid = fidelity_engine.evaluate(obj, san)
                fidelity_scores.append(fid["preservation_score"])
                total_entities += len(ents)
                total_removed += rem
                for e in ents:
                    cat_counts[e.entity_type] += 1
                return san
            if isinstance(obj, list):
                return [_sanitize_obj(x) for x in obj]
            if isinstance(obj, dict):
                return {k: _sanitize_obj(v) for k, v in obj.items()}
            return obj

        sanitized_json = _sanitize_obj(payload)
        records_count = len(payload) if isinstance(payload, list) else 1
        sanitized_out = json.dumps(sanitized_json, ensure_ascii=False, indent=2)
        preview_rows = sanitized_json[:10] if isinstance(sanitized_json, list) else [sanitized_json]

    r_before, r_after, _ = risk_analyzer.analyze_batch(quasi_rows or [QuasiRecord()])
    avg_fid = round(sum(fidelity_scores) / len(fidelity_scores), 4) if fidelity_scores else 1.0
    dt = (time.perf_counter() - t0) * 1000.0

    audit_store.log_event(
        operation="batch_process",
        language="multi",
        records_count=records_count,
        entities_detected=total_entities,
        entities_removed=total_removed,
        fidelity_score=avg_fid,
        risk_before=r_before["reidentification_risk_score"],
        risk_after=r_after["reidentification_risk_score"],
        latency_ms=dt,
        category_counts=dict(cat_counts),
    )

    return BatchProcessResponse(
        filename=filename,
        format=ext,
        records_processed=records_count,
        entities_detected=total_entities,
        entities_removed=total_removed,
        avg_fidelity_score=avg_fid,
        risk_before=r_before,
        risk_after=r_after,
        preview_rows=preview_rows,
        sanitized_content=sanitized_out,
        latency_ms=round(dt, 2),
    )


@router.get("/metrics", response_model=MetricsResponse)
def get_metrics() -> MetricsResponse:
    return MetricsResponse(**audit_store.get_metrics())


@router.get("/evaluation/run")
def run_eval() -> Dict[str, Any]:
    return run_evaluation_suite()


@router.post("/privacy-defense/evaluate")
def evaluate_privacy_defense(n_patients: int = 36, seed: int = 42) -> Dict[str, Any]:
    safe_n = max(12, min(n_patients, 100))
    return run_reidentification_defense_lab(n_patients=safe_n, seed=seed)
