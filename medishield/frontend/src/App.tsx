import React, { useEffect, useMemo, useState } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { api, AnonymizeResponse, DetectedEntity, EvaluationResponse, MetricsResponse } from "./api";
import {
  AlertIcon,
  FlaskIcon,
  GridIcon,
  LayersIcon,
  LinkIcon,
  ListIcon,
  PulseIcon,
  ScanIcon,
  ShieldIcon,
  SlidersIcon,
} from "./components/Icons";

type TabId =
  | "overview"
  | "scanner"
  | "batch"
  | "risk"
  | "linkage"
  | "fidelity"
  | "audit"
  | "evaluation"
  | "settings";

const SAMPLE_RECORDS: Record<string, string> = {
  Hinglish:
    "Patient Rahul Sharma, aged 45, residing at MG Road, Bengaluru. Contact: 9876543210. Patient ko Type 2 Diabetes hai. Metformin 500 mg prescribed. Blood pressure: 130/85 mmHg.",
  Hindi:
    "रोगी: मीरा देवी, उम्र 47 साल, पता: रामपुर गाँव, PIN 226001. C/O राजन कुमार. Dengue diagnosed. Paracetamol 500 mg BD x 5 days.",
  Disambiguation:
    "Pt. Sunita Yadav, C/O fever and cough since 3 days. Dr. Rajesh Gupta advised Ramipril 5 mg OD and Dolo 650 mg 1-0-1. Email: sunita.yadav@example.in, PAN: ABCDE1234F.",
};

const CHART_COLORS = ["#0D9488", "#059669", "#0284C7", "#D97706", "#E11D48", "#64748B"];

function HighlightedText({ text, entities }: { text: string; entities: DetectedEntity[] }) {
  if (!entities.length) return <span>{text}</span>;
  const sorted = [...entities].sort((a, b) => a.start - b.start);
  const parts: React.ReactNode[] = [];
  let cursor = 0;

  sorted.forEach((ent, idx) => {
    if (ent.start > cursor) {
      parts.push(<span key={`t-${idx}`}>{text.slice(cursor, ent.start)}</span>);
    }
    parts.push(
      <mark
        key={`e-${idx}`}
        title={`${ent.entity_type} (${ent.method}, ${(ent.confidence * 100).toFixed(0)}%)`}
        className="rounded bg-amber-100 px-1 py-0.5 text-amber-900 border border-amber-300 font-medium"
      >
        {text.slice(ent.start, ent.end)}
      </mark>
    );
    cursor = ent.end;
  });
  if (cursor < text.length) {
    parts.push(<span key="tail">{text.slice(cursor)}</span>);
  }
  return <>{parts}</>;
}

export default function App() {
  const [tab, setTab] = useState<TabId>("overview");
  const [health, setHealth] = useState<{ status: string; offline_mode: boolean; llm_usage: boolean } | null>(null);
  const [metrics, setMetrics] = useState<MetricsResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const [inputText, setInputText] = useState(SAMPLE_RECORDS.Hinglish);
  const [policyMode, setPolicyMode] = useState("pseudonymization");
  const [ageBand, setAgeBand] = useState(5);
  const [scanEntities, setScanEntities] = useState<DetectedEntity[]>([]);
  const [scanLang, setScanLang] = useState("hinglish");
  const [anonResult, setAnonResult] = useState<AnonymizeResponse | null>(null);
  const [scannerBusy, setScannerBusy] = useState(false);

  const [batchResult, setBatchResult] = useState<Awaited<ReturnType<typeof api.batchProcess>> | null>(null);
  const [batchBusy, setBatchBusy] = useState(false);

  const [riskResult, setRiskResult] = useState<Awaited<ReturnType<typeof api.riskAnalyze>> | null>(null);
  const [genAge, setGenAge] = useState(true);
  const [genLoc, setGenLoc] = useState(true);
  const [suppressRare, setSuppressRare] = useState(true);

  const [linkageThreshold, setLinkageThreshold] = useState(0.72);
  const [linkageResult, setLinkageResult] = useState<Awaited<ReturnType<typeof api.linkageAnalyze>> | null>(null);

  const [fidelityOrig, setFidelityOrig] = useState(SAMPLE_RECORDS.Hinglish);
  const [fidelitySan, setFidelitySan] = useState("");
  const [fidelityResult, setFidelityResult] = useState<Awaited<ReturnType<typeof api.evaluateFidelity>> | null>(null);

  const [evalResult, setEvalResult] = useState<EvaluationResponse | null>(null);
  const [evalBusy, setEvalBusy] = useState(false);

  const refreshMetrics = async () => {
    try {
      const [h, m] = await Promise.all([api.health(), api.metrics()]);
      setHealth(h);
      setMetrics(m);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Backend unreachable");
    }
  };

  useEffect(() => {
    refreshMetrics();
  }, []);

  const handleScan = async () => {
    setScannerBusy(true);
    setError(null);
    try {
      const res = await api.scan(inputText);
      setScanEntities(res.entities);
      setScanLang(res.language);
      refreshMetrics();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Scan failed");
    } finally {
      setScannerBusy(false);
    }
  };

  const handleAnonymize = async () => {
    setScannerBusy(true);
    setError(null);
    try {
      const res = await api.anonymize(inputText, policyMode, ageBand);
      setAnonResult(res);
      setScanEntities(res.entities);
      setScanLang(res.language);
      setFidelityOrig(inputText);
      setFidelitySan(res.sanitized_text);
      refreshMetrics();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Anonymization failed");
    } finally {
      setScannerBusy(false);
    }
  };

  const handleBatchUpload = async (file: File) => {
    setBatchBusy(true);
    setError(null);
    try {
      const res = await api.batchProcess(file);
      setBatchResult(res);
      refreshMetrics();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Batch processing failed");
    } finally {
      setBatchBusy(false);
    }
  };

  const handleRunRisk = async () => {
    setError(null);
    try {
      const sampleBatch = [
        { age: 45, gender: "M", location: "MG Road, Bengaluru", occupation: "Engineer", diagnosis: "Type 2 Diabetes", visit_date: "2026-10-12" },
        { age: 46, gender: "M", location: "Indiranagar, Bengaluru", occupation: "Teacher", diagnosis: "Type 2 Diabetes", visit_date: "2026-10-18" },
        { age: 47, gender: "F", location: "Rampur, Lucknow", occupation: "Farmer", diagnosis: "Dengue", visit_date: "2026-10-21" },
        { age: 48, gender: "F", location: "Alambagh, Lucknow", occupation: "Clerk", diagnosis: "Dengue", visit_date: "2026-10-25" },
        { age: 62, gender: "M", location: "Sector 14, Gurugram", occupation: "Retired", diagnosis: "Rare Autoimmune Vasculitis", visit_date: "2026-11-02" },
      ];
      const res = await api.riskAnalyze(sampleBatch, genAge, genLoc, suppressRare);
      setRiskResult(res);
      refreshMetrics();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Risk analysis failed");
    }
  };

  const handleRunLinkage = async () => {
    setError(null);
    try {
      const sampleRecords = [
        { record_id: "R101", hospital: "HOSP_A", name: "Mohammad Arif", phone: "9811223344", age: 44, gender: "M" },
        { record_id: "R201", hospital: "HOSP_B", name: "मोहम्मद आरिफ", phone: "+91-9811223344", age: 44, gender: "M" },
        { record_id: "R301", hospital: "HOSP_C", name: "Md. Arif", phone: "9811223344", age: 45, gender: "M" },
        { record_id: "R102", hospital: "HOSP_A", name: "Sunita Yadav", phone: "9988776655", age: 38, gender: "F" },
      ];
      const res = await api.linkageAnalyze(sampleRecords, linkageThreshold);
      setLinkageResult(res);
      refreshMetrics();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Linkage analysis failed");
    }
  };

  const handleRunEvaluation = async () => {
    setEvalBusy(true);
    setError(null);
    try {
      const res = await api.runEvaluation();
      setEvalResult(res);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Evaluation failed");
    } finally {
      setEvalBusy(false);
    }
  };

  const categoryData = useMemo(
    () =>
      Object.entries(metrics?.category_distribution || {}).map(([name, value]) => ({
        name,
        value,
      })),
    [metrics]
  );

  const langData = useMemo(
    () =>
      Object.entries(metrics?.language_distribution || {}).map(([name, value]) => ({
        name,
        value,
      })),
    [metrics]
  );

  const navItems: Array<{ id: TabId; label: string; icon: React.ReactNode }> = [
    { id: "overview", label: "Overview", icon: <GridIcon /> },
    { id: "scanner", label: "Record Scanner", icon: <ScanIcon /> },
    { id: "batch", label: "Batch Processing", icon: <LayersIcon /> },
    { id: "risk", label: "Privacy Risk Analysis", icon: <AlertIcon /> },
    { id: "linkage", label: "Record Linkage", icon: <LinkIcon /> },
    { id: "fidelity", label: "Medical Fidelity", icon: <PulseIcon /> },
    { id: "audit", label: "Audit Logs", icon: <ListIcon /> },
    { id: "evaluation", label: "Evaluation Lab", icon: <FlaskIcon /> },
    { id: "settings", label: "Settings", icon: <SlidersIcon /> },
  ];

  return (
    <div className="min-h-screen flex bg-[#F4F7FA] text-slate-900">
      {/* Sidebar */}
      <aside className="w-64 shrink-0 border-r border-slate-200 bg-white flex flex-col shadow-xs">
        <div className="px-5 py-5 border-b border-slate-200 flex items-center gap-3">
          <div className="w-9 h-9 rounded-lg bg-teal-600 flex items-center justify-center text-white shadow-xs">
            <ShieldIcon className="w-5 h-5" />
          </div>
          <div>
            <div className="font-bold text-sm tracking-tight text-slate-900">MediShield</div>
            <div className="text-[11px] text-slate-500">Healthcare Privacy Firewall</div>
          </div>
        </div>

        <nav className="flex-1 px-3 py-4 space-y-1">
          {navItems.map((item) => {
            const active = tab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setTab(item.id)}
                className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm transition-colors duration-150 text-left ${
                  active
                    ? "bg-teal-50 text-teal-800 border border-teal-200 font-semibold"
                    : "text-slate-600 hover:text-slate-900 hover:bg-slate-100 border border-transparent"
                }`}
              >
                <span className={active ? "text-teal-600" : "text-slate-400"}>{item.icon}</span>
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>

        <div className="p-4 border-t border-slate-200 bg-slate-50/70 text-xs space-y-1.5">
          <div className="flex items-center justify-between">
            <span className="text-slate-500">Engine</span>
            <span className="font-mono font-semibold text-emerald-700">
              {health?.offline_mode ? "OFFLINE" : "CONNECTING"}
            </span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-slate-500">LLM Inference</span>
            <span className="font-mono font-semibold text-teal-700">DISABLED</span>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col min-w-0">
        <header className="h-14 border-b border-slate-200 bg-white px-6 flex items-center justify-between">
          <div className="text-sm font-semibold text-slate-800">
            {navItems.find((n) => n.id === tab)?.label}
          </div>
          <div className="flex items-center gap-3 text-xs">
            <span className="px-2.5 py-1 rounded-md bg-emerald-50 border border-emerald-200 text-emerald-800 font-mono font-medium">
              Zero-LLM · CPU Local
            </span>
            <button
              onClick={refreshMetrics}
              className="px-3 py-1.5 rounded-md border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 font-medium transition-colors"
            >
              Refresh Metrics
            </button>
          </div>
        </header>

        {error && (
          <div className="mx-6 mt-4 px-4 py-3 rounded-lg bg-rose-50 border border-rose-200 text-rose-800 text-sm">
            {error}
          </div>
        )}

        <div className="p-6 flex-1 overflow-y-auto space-y-6">
          {/* OVERVIEW */}
          {tab === "overview" && (
            <>
              <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
                {[
                  { label: "Records Processed", value: metrics?.total_records_processed ?? 0 },
                  { label: "PII Entities Detected", value: metrics?.total_entities_detected ?? 0 },
                  { label: "Identifiers Removed", value: metrics?.total_identifiers_removed ?? 0 },
                  {
                    label: "Avg Medical Fidelity",
                    value: `${((metrics?.avg_medical_fidelity ?? 1) * 100).toFixed(1)}%`,
                  },
                  { label: "Linkage Risks Flagged", value: metrics?.records_flagged_linkage ?? 0 },
                  { label: "Avg Latency", value: `${(metrics?.avg_latency_ms ?? 0).toFixed(1)} ms` },
                  {
                    label: "Avg Risk Reduction",
                    value: `${((metrics?.avg_risk_reduction ?? 0) * 100).toFixed(1)}%`,
                  },
                  { label: "Audit Events", value: metrics?.recent_activity.length ?? 0 },
                ].map((stat) => (
                  <div key={stat.label} className="rounded-xl border border-slate-200 bg-white p-4 shadow-xs">
                    <div className="text-xs font-medium text-slate-500">{stat.label}</div>
                    <div className="mt-1.5 text-2xl font-bold font-mono text-slate-900">{stat.value}</div>
                  </div>
                ))}
              </div>

              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-xs">
                  <h3 className="text-sm font-semibold text-slate-800 mb-4">PII Category Distribution</h3>
                  {categoryData.length === 0 ? (
                    <div className="h-56 flex items-center justify-center text-sm text-slate-400">
                      Run a scan, anonymization, or batch job to populate real category counts.
                    </div>
                  ) : (
                    <div className="h-56">
                      <ResponsiveContainer width="100%" height="100%">
                        <BarChart data={categoryData}>
                          <CartesianGrid strokeDasharray="3 3" stroke="#E2E8F0" />
                          <XAxis dataKey="name" stroke="#64748B" fontSize={11} />
                          <YAxis stroke="#64748B" fontSize={11} />
                          <Tooltip contentStyle={{ backgroundColor: "#FFFFFF", borderColor: "#CBD5E1", color: "#0F172A" }} />
                          <Bar dataKey="value" fill="#0D9488" radius={[4, 4, 0, 0]} />
                        </BarChart>
                      </ResponsiveContainer>
                    </div>
                  )}
                </div>

                <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-xs">
                  <h3 className="text-sm font-semibold text-slate-800 mb-4">Language Distribution</h3>
                  {langData.length === 0 ? (
                    <div className="h-56 flex items-center justify-center text-sm text-slate-400">
                      No processed records yet.
                    </div>
                  ) : (
                    <div className="h-56">
                      <ResponsiveContainer width="100%" height="100%">
                        <PieChart>
                          <Pie data={langData} dataKey="value" nameKey="name" outerRadius={80} label>
                            {langData.map((_, i) => (
                              <Cell key={i} fill={CHART_COLORS[i % CHART_COLORS.length]} />
                            ))}
                          </Pie>
                          <Tooltip contentStyle={{ backgroundColor: "#FFFFFF", borderColor: "#CBD5E1", color: "#0F172A" }} />
                        </PieChart>
                      </ResponsiveContainer>
                    </div>
                  )}
                </div>
              </div>
            </>
          )}

          {/* RECORD SCANNER */}
          {tab === "scanner" && (
            <div className="space-y-5">
              <div className="flex flex-wrap items-center justify-between gap-3">
                <div className="flex items-center gap-2">
                  {Object.entries(SAMPLE_RECORDS).map(([label, text]) => (
                    <button
                      key={label}
                      onClick={() => setInputText(text)}
                      className="px-3 py-1.5 rounded-lg text-xs font-medium border border-slate-200 bg-white hover:border-teal-400 text-slate-700 shadow-xs"
                    >
                      Load {label} Sample
                    </button>
                  ))}
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-xs font-mono px-2.5 py-1 rounded-md bg-teal-50 border border-teal-200 text-teal-800">
                    Lang: {scanLang}
                  </span>
                  <button
                    onClick={handleScan}
                    disabled={scannerBusy}
                    className="px-3.5 py-1.5 rounded-lg text-xs font-semibold border border-slate-300 bg-white hover:bg-slate-50 text-slate-700"
                  >
                    Scan PII
                  </button>
                  <button
                    onClick={handleAnonymize}
                    disabled={scannerBusy}
                    className="px-4 py-1.5 rounded-lg text-xs font-semibold bg-teal-600 hover:bg-teal-700 text-white shadow-xs"
                  >
                    {scannerBusy ? "Processing..." : "Anonymize"}
                  </button>
                </div>
              </div>

              {/* Split Screen */}
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">
                <div className="rounded-xl border border-slate-200 bg-white p-4 space-y-3 shadow-xs">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-semibold uppercase tracking-wider text-slate-500">
                      Original Record (Editable + Highlighted)
                    </span>
                    <span className="text-xs font-mono font-semibold text-amber-700 bg-amber-50 px-2 py-0.5 rounded border border-amber-200">
                      {scanEntities.length} entities
                    </span>
                  </div>
                  <textarea
                    rows={5}
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    className="w-full rounded-lg bg-slate-50 border border-slate-200 p-3 text-sm font-mono text-slate-800 focus:outline-none focus:border-teal-500"
                  />
                  <div className="rounded-lg bg-slate-50 border border-slate-200 p-3 text-sm leading-relaxed text-slate-800">
                    <HighlightedText text={inputText} entities={scanEntities} />
                  </div>
                </div>

                <div className="rounded-xl border border-slate-200 bg-white p-4 space-y-3 shadow-xs">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-semibold uppercase tracking-wider text-slate-500">
                      Sanitized Output
                    </span>
                    <div className="flex gap-2">
                      <button
                        onClick={() => anonResult && navigator.clipboard.writeText(anonResult.sanitized_text)}
                        className="px-2.5 py-1 rounded-md text-xs font-medium border border-slate-200 hover:bg-slate-50 text-slate-700"
                      >
                        Copy
                      </button>
                      <button
                        onClick={() => {
                          if (!anonResult) return;
                          const blob = new Blob([anonResult.sanitized_text], { type: "text/plain" });
                          const url = URL.createObjectURL(blob);
                          const a = document.createElement("a");
                          a.href = url;
                          a.download = "sanitized_record.txt";
                          a.click();
                        }}
                        className="px-2.5 py-1 rounded-md text-xs font-medium border border-teal-200 bg-teal-50 text-teal-800 hover:bg-teal-100"
                      >
                        Export
                      </button>
                    </div>
                  </div>
                  <div className="min-h-[160px] rounded-lg bg-emerald-50/50 border border-emerald-200 p-3 text-sm font-mono text-emerald-900 whitespace-pre-wrap">
                    {anonResult ? anonResult.sanitized_text : "Click 'Anonymize' to generate privacy-safe output."}
                  </div>

                  {anonResult && (
                    <div className="grid grid-cols-3 gap-3 text-xs">
                      <div className="rounded-lg bg-rose-50 border border-rose-200 p-2.5">
                        <div className="text-rose-700 font-medium">Risk Before</div>
                        <div className="font-mono font-bold text-rose-900 text-sm mt-0.5">
                          {String(anonResult.risk_before.reidentification_risk_score)} ({String(anonResult.risk_before.risk_level)})
                        </div>
                      </div>
                      <div className="rounded-lg bg-emerald-50 border border-emerald-200 p-2.5">
                        <div className="text-emerald-700 font-medium">Risk After</div>
                        <div className="font-mono font-bold text-emerald-900 text-sm mt-0.5">
                          {String(anonResult.risk_after.reidentification_risk_score)} ({String(anonResult.risk_after.risk_level)})
                        </div>
                      </div>
                      <div className="rounded-lg bg-teal-50 border border-teal-200 p-2.5">
                        <div className="text-teal-700 font-medium">Medical Fidelity</div>
                        <div className="font-mono font-bold text-teal-900 text-sm mt-0.5">
                          {(anonResult.fidelity.preservation_score * 100).toFixed(0)}% ({anonResult.fidelity.preserved_items.length}/{anonResult.fidelity.total_clinical_items})
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              </div>

              {/* Detected Entities Table */}
              <div className="rounded-xl border border-slate-200 bg-white overflow-hidden shadow-xs">
                <div className="px-4 py-3 border-b border-slate-200 text-xs font-semibold uppercase tracking-wider text-slate-500">
                  Detected Entities
                </div>
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-50 text-slate-600 border-b border-slate-200">
                    <tr>
                      <th className="px-4 py-2.5">Type</th>
                      <th className="px-4 py-2.5">Matched Span</th>
                      <th className="px-4 py-2.5">Offsets</th>
                      <th className="px-4 py-2.5">Method</th>
                      <th className="px-4 py-2.5">Confidence</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-200">
                    {scanEntities.map((e, i) => (
                      <tr key={i} className="hover:bg-slate-50">
                        <td className="px-4 py-2 font-mono font-semibold text-teal-700">{e.entity_type}</td>
                        <td className="px-4 py-2 font-mono text-amber-800">{e.text}</td>
                        <td className="px-4 py-2 font-mono text-slate-500">
                          {e.start}..{e.end}
                        </td>
                        <td className="px-4 py-2 text-slate-700">{e.method}</td>
                        <td className="px-4 py-2 font-mono font-semibold text-emerald-700">{(e.confidence * 100).toFixed(0)}%</td>
                      </tr>
                    ))}
                    {scanEntities.length === 0 && (
                      <tr>
                        <td colSpan={5} className="px-4 py-6 text-center text-slate-400">
                          No entities scanned yet.
                        </td>
                      </tr>
                    )}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* BATCH PROCESSING */}
          {tab === "batch" && (
            <div className="space-y-5">
              <div className="rounded-xl border border-dashed border-slate-300 bg-white p-6 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-xs">
                <div>
                  <h3 className="text-sm font-semibold text-slate-900">Upload Hospital Record File (CSV, JSON, TXT)</h3>
                  <p className="text-xs text-slate-500 mt-1">
                    Processed 100% offline in memory. Original identifiers are never logged.
                  </p>
                </div>
                <input
                  type="file"
                  accept=".csv,.json,.txt"
                  disabled={batchBusy}
                  onChange={(e) => {
                    const f = e.target.files?.[0];
                    if (f) handleBatchUpload(f);
                  }}
                  className="text-xs text-slate-600 file:mr-3 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-teal-600 file:text-white file:font-semibold hover:file:bg-teal-700"
                />
              </div>

              {batchResult && (
                <div className="space-y-4">
                  <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-xs">
                      <div className="text-slate-500">Records Processed</div>
                      <div className="text-xl font-mono font-bold text-slate-900 mt-1">{batchResult.records_processed}</div>
                    </div>
                    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-xs">
                      <div className="text-slate-500">Identifiers Removed</div>
                      <div className="text-xl font-mono font-bold text-teal-700 mt-1">{batchResult.entities_removed}</div>
                    </div>
                    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-xs">
                      <div className="text-slate-500">Avg Medical Fidelity</div>
                      <div className="text-xl font-mono font-bold text-emerald-700 mt-1">
                        {(batchResult.avg_fidelity_score * 100).toFixed(1)}%
                      </div>
                    </div>
                    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-xs">
                      <div className="text-slate-500">Latency</div>
                      <div className="text-xl font-mono font-bold text-slate-900 mt-1">{batchResult.latency_ms} ms</div>
                    </div>
                  </div>
                  <div className="rounded-xl border border-slate-200 bg-white p-4 space-y-3 shadow-xs">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-semibold uppercase text-slate-500">Sanitized Output Preview</span>
                      <button
                        onClick={() => {
                          const blob = new Blob([batchResult.sanitized_content], { type: "text/plain" });
                          const url = URL.createObjectURL(blob);
                          const a = document.createElement("a");
                          a.href = url;
                          a.download = `sanitized_${batchResult.filename}`;
                          a.click();
                        }}
                        className="px-3 py-1.5 rounded-lg bg-teal-600 text-white text-xs font-semibold hover:bg-teal-700"
                      >
                        Download Sanitized File
                      </button>
                    </div>
                    <pre className="p-3 rounded-lg bg-slate-50 border border-slate-200 text-xs font-mono text-emerald-900 overflow-x-auto max-h-80">
                      {batchResult.sanitized_content}
                    </pre>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* PRIVACY RISK ANALYSIS */}
          {tab === "risk" && (
            <div className="space-y-5">
              <div className="rounded-xl border border-slate-200 bg-white p-5 flex flex-wrap items-center justify-between gap-4 shadow-xs">
                <div className="flex flex-wrap gap-4 text-xs text-slate-700">
                  <label className="flex items-center gap-2">
                    <input type="checkbox" checked={genAge} onChange={(e) => setGenAge(e.target.checked)} />
                    5-Year Age Banding
                  </label>
                  <label className="flex items-center gap-2">
                    <input type="checkbox" checked={genLoc} onChange={(e) => setGenLoc(e.target.checked)} />
                    City/Region Generalization
                  </label>
                  <label className="flex items-center gap-2">
                    <input type="checkbox" checked={suppressRare} onChange={(e) => setSuppressRare(e.target.checked)} />
                    Suppress Rare Diagnoses
                  </label>
                </div>
                <button
                  onClick={handleRunRisk}
                  className="px-4 py-2 rounded-lg bg-teal-600 hover:bg-teal-700 text-white text-xs font-semibold"
                >
                  Run k-Anonymity Risk Analysis
                </button>
              </div>

              {riskResult && (
                <div className="space-y-4">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="rounded-xl border border-rose-200 bg-white p-4 space-y-2 text-xs shadow-xs">
                      <div className="font-semibold text-rose-700">Before Transformation</div>
                      <pre className="font-mono text-slate-800">{JSON.stringify(riskResult.risk_before, null, 2)}</pre>
                    </div>
                    <div className="rounded-xl border border-emerald-200 bg-white p-4 space-y-2 text-xs shadow-xs">
                      <div className="font-semibold text-emerald-700">After Transformation</div>
                      <pre className="font-mono text-slate-800">{JSON.stringify(riskResult.risk_after, null, 2)}</pre>
                    </div>
                  </div>
                  <div className="rounded-xl border border-amber-200 bg-amber-50 p-4 text-xs text-amber-900">
                    <strong>Heuristic Note:</strong> {riskResult.disclaimer}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* RECORD LINKAGE */}
          {tab === "linkage" && (
            <div className="space-y-5">
              <div className="rounded-xl border border-slate-200 bg-white p-5 flex items-center justify-between shadow-xs">
                <div className="flex items-center gap-4 text-xs">
                  <span className="text-slate-700 font-medium">Similarity Threshold:</span>
                  <input
                    type="range"
                    min={0.5}
                    max={0.95}
                    step={0.01}
                    value={linkageThreshold}
                    onChange={(e) => setLinkageThreshold(parseFloat(e.target.value))}
                  />
                  <span className="font-mono font-semibold text-teal-700">{linkageThreshold.toFixed(2)}</span>
                </div>
                <button
                  onClick={handleRunLinkage}
                  className="px-4 py-2 rounded-lg bg-teal-600 hover:bg-teal-700 text-white text-xs font-semibold"
                >
                  Analyze Cross-Hospital Linkage
                </button>
              </div>

              {linkageResult && (
                <div className="space-y-4">
                  <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-xs">
                    <h4 className="text-xs font-semibold uppercase text-slate-500 mb-3">
                      Pseudonymized Clusters ({linkageResult.clusters.length})
                    </h4>
                    <div className="space-y-2 text-xs">
                      {linkageResult.clusters.map((c) => (
                        <div key={c.cluster_id} className="p-3 rounded-lg bg-slate-50 border border-slate-200 flex flex-wrap justify-between gap-2">
                          <span className="font-mono font-semibold text-teal-700">{c.pseudonym}</span>
                          <span className="font-mono text-slate-700">Records: {c.record_ids.join(", ")}</span>
                          <span className="text-slate-600">Hospitals: {c.hospitals.join(", ")}</span>
                          <span className="font-mono font-semibold text-emerald-700">Confidence: {c.avg_confidence}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                  <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-xs">
                    <h4 className="text-xs font-semibold uppercase text-slate-500 mb-3">
                      Flagged Pairs ({linkageResult.flagged_pairs.length})
                    </h4>
                    <div className="space-y-2 text-xs">
                      {linkageResult.flagged_pairs.map((p, i) => (
                        <div key={i} className="p-3 rounded-lg bg-slate-50 border border-slate-200 flex justify-between">
                          <span className="font-mono text-slate-800">
                            {p.record_a} ({p.hospital_a}) ↔ {p.record_b} ({p.hospital_b})
                          </span>
                          <span className="text-slate-600">{p.reasons.join(" · ")}</span>
                          <span className="font-mono font-semibold text-amber-700">Score: {p.score}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* MEDICAL FIDELITY */}
          {tab === "fidelity" && (
            <div className="space-y-4">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                <textarea
                  rows={5}
                  value={fidelityOrig}
                  onChange={(e) => setFidelityOrig(e.target.value)}
                  placeholder="Original clinical text..."
                  className="rounded-xl bg-white border border-slate-200 p-3 text-xs font-mono text-slate-800 shadow-xs"
                />
                <textarea
                  rows={5}
                  value={fidelitySan}
                  onChange={(e) => setFidelitySan(e.target.value)}
                  placeholder="Sanitized text..."
                  className="rounded-xl bg-white border border-slate-200 p-3 text-xs font-mono text-slate-800 shadow-xs"
                />
              </div>
              <button
                onClick={async () => {
                  const res = await api.evaluateFidelity(fidelityOrig, fidelitySan || fidelityOrig);
                  setFidelityResult(res);
                }}
                className="px-4 py-2 rounded-lg bg-teal-600 hover:bg-teal-700 text-white text-xs font-semibold"
              >
                Evaluate Medical Fidelity
              </button>
              {fidelityResult && (
                <div className="rounded-xl border border-slate-200 bg-white p-4 text-xs space-y-2 shadow-xs">
                  <div className="font-mono font-bold text-lg text-emerald-700">
                    Preservation Score: {(fidelityResult.preservation_score * 100).toFixed(1)}%
                  </div>
                  <div className="text-slate-700">
                    Preserved: {fidelityResult.preserved_items.map((x) => x.value).join(", ") || "None"}
                  </div>
                  {fidelityResult.lost_items.length > 0 && (
                    <div className="text-rose-700">
                      Lost: {fidelityResult.lost_items.map((x) => x.value).join(", ")}
                    </div>
                  )}
                </div>
              )}
            </div>
          )}

          {/* AUDIT LOGS */}
          {tab === "audit" && (
            <div className="rounded-xl border border-slate-200 bg-white overflow-hidden shadow-xs">
              <div className="px-4 py-3 border-b border-slate-200 text-xs font-medium text-slate-500">
                Sanitized Metadata Only (Zero raw PII stored)
              </div>
              <table className="w-full text-left text-xs">
                <thead className="bg-slate-50 text-slate-600 border-b border-slate-200">
                  <tr>
                    <th className="px-4 py-2.5">Timestamp</th>
                    <th className="px-4 py-2.5">Operation</th>
                    <th className="px-4 py-2.5">Language</th>
                    <th className="px-4 py-2.5">Detected</th>
                    <th className="px-4 py-2.5">Removed</th>
                    <th className="px-4 py-2.5">Fidelity</th>
                    <th className="px-4 py-2.5">Latency</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-200 font-mono">
                  {(metrics?.recent_activity || []).map((r) => (
                    <tr key={r.id} className="hover:bg-slate-50">
                      <td className="px-4 py-2 text-slate-500">{r.created_at.slice(0, 19)}</td>
                      <td className="px-4 py-2 font-semibold text-teal-700">{r.operation}</td>
                      <td className="px-4 py-2 text-slate-700">{r.language}</td>
                      <td className="px-4 py-2 text-slate-800">{r.entities_detected}</td>
                      <td className="px-4 py-2 text-slate-800">{r.entities_removed}</td>
                      <td className="px-4 py-2 font-semibold text-emerald-700">{(r.fidelity_score * 100).toFixed(0)}%</td>
                      <td className="px-4 py-2 text-slate-700">{r.latency_ms} ms</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {/* EVALUATION LAB */}
          {tab === "evaluation" && (
            <div className="space-y-5">
              <div className="flex items-center justify-between">
                <div className="text-xs text-slate-600">
                  Runs real offline English, Hindi & Hinglish test suite with edge-case disambiguation.
                </div>
                <button
                  onClick={handleRunEvaluation}
                  disabled={evalBusy}
                  className="px-4 py-2 rounded-lg bg-teal-600 hover:bg-teal-700 text-white text-xs font-semibold"
                >
                  {evalBusy ? "Running..." : "Run Evaluation Suite"}
                </button>
              </div>
              {evalResult && (
                <>
                  <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
                    {[
                      { k: "Precision", v: `${(evalResult.precision * 100).toFixed(1)}%` },
                      { k: "Recall", v: `${(evalResult.recall * 100).toFixed(1)}%` },
                      { k: "F1 Score", v: `${(evalResult.f1_score * 100).toFixed(1)}%` },
                      { k: "PII Leakage Rate", v: `${(evalResult.pii_leakage_rate * 100).toFixed(1)}%` },
                      { k: "False Positive Rate", v: `${(evalResult.false_positive_rate * 100).toFixed(1)}%` },
                      { k: "Medical Preservation", v: `${(evalResult.medical_preservation_rate * 100).toFixed(1)}%` },
                      { k: "Linkage Accuracy", v: `${(evalResult.record_linkage_accuracy * 100).toFixed(1)}%` },
                      { k: "Avg Latency", v: `${evalResult.avg_latency_ms} ms` },
                    ].map((m) => (
                      <div key={m.k} className="rounded-xl border border-slate-200 bg-white p-4 shadow-xs">
                        <div className="text-xs text-slate-500">{m.k}</div>
                        <div className="text-xl font-mono font-bold text-emerald-700 mt-1">{m.v}</div>
                      </div>
                    ))}
                  </div>
                  <div className="space-y-3">
                    {evalResult.cases.map((c) => (
                      <div key={c.id} className="rounded-xl border border-slate-200 bg-white p-4 text-xs space-y-2 shadow-xs">
                        <div className="flex justify-between font-mono">
                          <span className="font-semibold text-teal-700">{c.id} ({c.detected_language})</span>
                          <span className="text-slate-600">Matched {c.matched}/{c.expected_count} · Fidelity {(c.medical_preservation * 100).toFixed(0)}% · {c.latency_ms} ms</span>
                        </div>
                        <div className="font-mono text-slate-800 bg-slate-50 p-2.5 rounded-lg border border-slate-200">
                          {c.sanitized_preview}
                        </div>
                      </div>
                    ))}
                  </div>
                </>
              )}
            </div>
          )}

          {/* SETTINGS */}
          {tab === "settings" && (
            <div className="rounded-xl border border-slate-200 bg-white p-5 space-y-4 max-w-xl text-xs shadow-xs">
              <div className="font-semibold text-sm text-slate-900">Default Anonymization Policy</div>
              <div className="space-y-1.5">
                <label className="text-slate-600 block font-medium">Default Transformation Mode</label>
                <select
                  value={policyMode}
                  onChange={(e) => setPolicyMode(e.target.value)}
                  className="w-full rounded-lg bg-slate-50 border border-slate-300 px-3 py-2 text-slate-800"
                >
                  <option value="pseudonymization">Pseudonymization (HMAC-SHA256)</option>
                  <option value="redaction">Redaction ([ENTITY_REDACTED])</option>
                  <option value="masking">Masking (Ra***ma)</option>
                  <option value="generalization">Generalization (Age Bands / Region)</option>
                  <option value="suppression">Suppression ([SUPPRESSED])</option>
                </select>
              </div>
              <div className="space-y-1.5">
                <label className="text-slate-600 block font-medium">Age Band Width (Years): {ageBand}</label>
                <input
                  type="range"
                  min={2}
                  max={10}
                  value={ageBand}
                  onChange={(e) => setAgeBand(parseInt(e.target.value, 10))}
                />
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
