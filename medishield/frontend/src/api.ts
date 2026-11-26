export interface DetectedEntity {
  entity_type: string;
  text: string;
  start: number;
  end: number;
  method: string;
  confidence: number;
  language: string;
}

export interface AnonymizeResponse {
  language: string;
  original_length: number;
  sanitized_text: string;
  entities: DetectedEntity[];
  transformations_applied: number;
  risk_before: Record<string, number | string>;
  risk_after: Record<string, number | string>;
  fidelity: {
    preservation_score: number;
    total_clinical_items: number;
    preserved_items: Array<{ category: string; value: string }>;
    lost_items: Array<{ category: string; value: string }>;
    breakdown: Record<string, { total: number; preserved: number; lost: number }>;
  };
  latency_ms: number;
}

export interface MetricsResponse {
  total_records_processed: number;
  total_entities_detected: number;
  total_identifiers_removed: number;
  records_flagged_linkage: number;
  avg_medical_fidelity: number;
  avg_latency_ms: number;
  avg_risk_reduction: number;
  category_distribution: Record<string, number>;
  language_distribution: Record<string, number>;
  recent_activity: Array<{
    id: number;
    created_at: string;
    operation: string;
    language: string;
    records_count: number;
    entities_detected: number;
    entities_removed: number;
    fidelity_score: number;
    risk_before: number;
    risk_after: number;
    latency_ms: number;
  }>;
}

export interface EvaluationResponse {
  precision: number;
  recall: number;
  f1_score: number;
  pii_leakage_rate: number;
  false_positive_rate: number;
  medical_preservation_rate: number;
  record_linkage_accuracy: number;
  avg_latency_ms: number;
  linkage_clusters_found: number;
  linkage_pairs_flagged: number;
  cases: Array<{
    id: string;
    detected_language: string;
    entities_found: number;
    expected_count: number;
    matched: number;
    medical_preservation: number;
    fidelity_engine_score: number;
    latency_ms: number;
    sanitized_preview: string;
  }>;
}

export interface PrivacyDefenseResponse {
  total_records: number;
  synthetic_patients: number;
  distinct_patients?: number;
  synthetic_voters: number;
  hospital_systems: string[];
  before_reidentification_rate: number;
  after_reidentification_rate: number;
  unique_confident_reid_rate?: number;
  forced_top_match_accuracy?: number;
  random_guess_baseline?: number;
  attacker_coverage?: number;
  age_band_size?: number;
  risk_reduction_pct: number;
  before_unique_rate: number;
  after_unique_rate: number;
  min_anonymity_group_size: number;
  avg_anonymity_group_size: number;
  record_level_min_k?: number;
  record_level_avg_k?: number;
  direct_pii_leakage_rate: number;
  residual_qi_exposure_rate: number;
  clinical_preservation_score: number;
  system_breakdown: Record<
    string,
    { records: number; before_reid: number; after_reid: number; direct_leaks: number }
  >;
  latency_ms: number;
  remaining_limitations?: string[];
  disclaimer: string;
}

export interface MetadataInspectResponse {
  traversal_blocked: boolean;
  filename_pii_detected: boolean;
  sanitized_filename: string;
  directory_pii_detected: boolean;
  sanitized_directory: string;
  headers: Array<{ original: string; sanitized: string; pii_detected: string }>;
  sanitized_json_preview: unknown;
  quarantine_rules: string[];
  latency_ms: number;
}

const BASE = "/api";

async function req<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${path}`, init);
  if (!res.ok) {
    const errText = await res.text();
    throw new Error(errText || `HTTP ${res.status}`);
  }
  return res.json() as Promise<T>;
}

export const api = {
  health: () => req<{ status: string; offline_mode: boolean; llm_usage: boolean }>("/health"),
  metrics: () => req<MetricsResponse>("/metrics"),
  scan: (text: string) =>
    req<{ language: string; entities: DetectedEntity[]; entity_counts: Record<string, number>; latency_ms: number }>("/scan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    }),
  anonymize: (text: string, default_mode: string, age_band_size: number) =>
    req<AnonymizeResponse>("/anonymize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, policy: { default_mode, age_band_size } }),
    }),
  batchProcess: (file: File) => {
    const fd = new FormData();
    fd.append("file", file);
    return req<{
      filename: string;
      format: string;
      records_processed: number;
      entities_detected: number;
      entities_removed: number;
      avg_fidelity_score: number;
      risk_before: Record<string, number | string>;
      risk_after: Record<string, number | string>;
      preview_rows: Array<Record<string, unknown>>;
      sanitized_content: string;
      latency_ms: number;
    }>("/batch-process", { method: "POST", body: fd });
  },
  linkageAnalyze: (records: unknown[], threshold: number) =>
    req<{
      total_records: number;
      candidate_pairs_evaluated: number;
      flagged_pairs: Array<{
        record_a: string;
        record_b: string;
        hospital_a: string;
        hospital_b: string;
        score: number;
        field_scores: Record<string, number>;
        reasons: string[];
      }>;
      clusters: Array<{
        cluster_id: string;
        pseudonym: string;
        record_ids: string[];
        hospitals: string[];
        avg_confidence: number;
      }>;
      latency_ms: number;
    }>("/linkage/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ records, threshold }),
    }),
  riskAnalyze: (records: unknown[], generalize_age: boolean, generalize_location: boolean, suppress_rare: boolean) =>
    req<{
      risk_before: Record<string, number | string>;
      risk_after: Record<string, number | string>;
      suggestions: string[];
      disclaimer: string;
      latency_ms: number;
    }>("/risk/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ records, generalize_age, generalize_location, suppress_rare }),
    }),
  evaluateFidelity: (original_text: string, sanitized_text: string) =>
    req<{
      preservation_score: number;
      total_clinical_items: number;
      preserved_items: Array<{ category: string; value: string }>;
      lost_items: Array<{ category: string; value: string }>;
      breakdown: Record<string, { total: number; preserved: number; lost: number }>;
      latency_ms: number;
    }>("/fidelity/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ original_text, sanitized_text }),
    }),
  runEvaluation: () => req<EvaluationResponse>("/evaluation/run"),
  evaluatePrivacyDefense: (n_patients = 100, seed = 42, age_band_size = 10) =>
    req<PrivacyDefenseResponse>(
      `/privacy-defense/evaluate?n_patients=${n_patients}&seed=${seed}&age_band_size=${age_band_size}`,
      { method: "POST" }
    ),
  inspectMetadata: (payload: {
    filename: string;
    directory: string;
    headers: string[];
    json_sample: unknown;
  }) =>
    req<MetadataInspectResponse>("/metadata/inspect", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    }),
};
