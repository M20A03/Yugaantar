"""Pydantic v2 request and response schemas for MediShield API."""

from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field


TransformMode = Literal["redaction", "masking", "pseudonymization", "generalization", "suppression"]


class DetectedEntity(BaseModel):
    entity_type: str
    text: str
    start: int
    end: int
    method: str
    confidence: float = Field(ge=0.0, le=1.0)
    language: str = "en"


class ScanRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=200_000)
    language_hint: Optional[str] = None


class ScanResponse(BaseModel):
    language: str
    entities: List[DetectedEntity]
    entity_counts: Dict[str, int]
    latency_ms: float


class PolicyConfig(BaseModel):
    default_mode: TransformMode = "pseudonymization"
    entity_modes: Dict[str, TransformMode] = Field(default_factory=dict)
    age_band_size: int = Field(default=5, ge=2, le=20)
    date_shift_days: int = Field(default=0, ge=-365, le=365)


class AnonymizeRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=200_000)
    policy: PolicyConfig = Field(default_factory=PolicyConfig)
    record_id: Optional[str] = None


class AnonymizeResponse(BaseModel):
    language: str
    original_length: int
    sanitized_text: str
    entities: List[DetectedEntity]
    transformations_applied: int
    risk_before: Dict[str, Any]
    risk_after: Dict[str, Any]
    fidelity: Dict[str, Any]
    latency_ms: float


class HospitalRecordInput(BaseModel):
    record_id: str
    hospital: str = "HOSP_A"
    name: Optional[str] = None
    phone: Optional[str] = None
    dob: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    mrn: Optional[str] = None
    raw_note: Optional[str] = None


class LinkageRequest(BaseModel):
    records: List[HospitalRecordInput] = Field(..., min_length=2, max_length=500)
    threshold: float = Field(default=0.72, ge=0.3, le=0.99)


class LinkagePair(BaseModel):
    record_a: str
    record_b: str
    hospital_a: str
    hospital_b: str
    score: float
    field_scores: Dict[str, float]
    reasons: List[str]


class LinkageCluster(BaseModel):
    cluster_id: str
    pseudonym: str
    record_ids: List[str]
    hospitals: List[str]
    avg_confidence: float


class LinkageResponse(BaseModel):
    total_records: int
    candidate_pairs_evaluated: int
    flagged_pairs: List[LinkagePair]
    clusters: List[LinkageCluster]
    latency_ms: float


class QuasiRecord(BaseModel):
    age: Optional[int] = None
    gender: Optional[str] = None
    location: Optional[str] = None
    occupation: Optional[str] = None
    diagnosis: Optional[str] = None
    visit_date: Optional[str] = None


class RiskAnalyzeRequest(BaseModel):
    records: List[QuasiRecord] = Field(..., min_length=1, max_length=2000)
    generalize_age: bool = True
    generalize_location: bool = True
    suppress_rare: bool = True
    rare_threshold: int = Field(default=2, ge=1, le=20)


class RiskAnalyzeResponse(BaseModel):
    risk_before: Dict[str, Any]
    risk_after: Dict[str, Any]
    suggestions: List[str]
    disclaimer: str
    latency_ms: float


class FidelityRequest(BaseModel):
    original_text: str = Field(..., min_length=1, max_length=200_000)
    sanitized_text: str = Field(..., min_length=1, max_length=200_000)


class FidelityResponse(BaseModel):
    preservation_score: float
    total_clinical_items: int
    preserved_items: List[Dict[str, str]]
    lost_items: List[Dict[str, str]]
    breakdown: Dict[str, Dict[str, int]]
    latency_ms: float


class BatchProcessResponse(BaseModel):
    filename: str
    format: str
    records_processed: int
    entities_detected: int
    entities_removed: int
    avg_fidelity_score: float
    risk_before: Dict[str, Any]
    risk_after: Dict[str, Any]
    preview_rows: List[Dict[str, Any]]
    sanitized_content: str
    latency_ms: float


class MetricsResponse(BaseModel):
    total_records_processed: int
    total_entities_detected: int
    total_identifiers_removed: int
    records_flagged_linkage: int
    avg_medical_fidelity: float
    avg_latency_ms: float
    avg_risk_reduction: float
    category_distribution: Dict[str, int]
    language_distribution: Dict[str, int]
    recent_activity: List[Dict[str, Any]]
