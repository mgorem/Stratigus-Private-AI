import { useEffect, useState } from "react";
import { createRun, executeRun, getRun, listRuns } from "./api";

const MODES = ["Summarise", "Key Points", "Security Analysis", "Free"];

export default function App() {
  const [input, setInput] = useState("");
  const [mode, setMode] = useState(MODES[0]);

  const [noStore, setNoStore] = useState(false);
  const [redactBeforeStore, setRedactBeforeStore] = useState(true);

  const [runs, setRuns] = useState([]);
  const [activeRun, setActiveRun] = useState(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function refreshRuns() {
    const data = await listRuns();
    setRuns(data);
  }

  useEffect(() => {
    refreshRuns().catch(() => { });
  }, []);

  async function openRun(runId) {
    setError("");
    try {
      const detail = await getRun(runId);
      setActiveRun(detail);
    } catch (e) {
      setError(e.message || String(e));
    }
  }

  async function onRun() {
    setError("");
    setLoading(true);

    try {
      const basePayload = {
        input,
        mode,
        no_store: noStore,
        redact_before_store: redactBeforeStore,
        require_confirm_if_pii: true,
        confirmed_pii: false
      };

      let created = await createRun(basePayload);

      if (created.requires_confirmation) {
        const details = (created.findings || [])
          .map(f => `- ${f.kind}: ${f.sample}`)
          .join("\n");

        const ok = window.confirm(
          `Privacy warning:\n\n${created.message}\n\nDetected:\n${details}\n\nProceed?`
        );

        if (!ok) {
          setLoading(false);
          return;
        }

        created = await createRun({ ...basePayload, confirmed_pii: true });
      }

      await refreshRuns();

      const exec = await executeRun(created.run_id);

      if (exec.result) {
        setActiveRun({
          id: created.run_id,
          mode,
          input_text: noStore ? "(not stored)" : input,
          status: exec.status,
          result: exec.result,
          error: null
        });
      } else {
        const detail = await getRun(created.run_id);
        setActiveRun(detail);
      }

      await refreshRuns();
    } catch (e) {
      setError(e.message || String(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ minHeight: "100vh", background: "#f6f7fb", padding: 20 }}>
      <div style={{ maxWidth: 1200, margin: "0 auto", display: "grid", gridTemplateColumns: "360px 1fr", gap: 16 }}>
        {/* LEFT */}
        <div style={{ background: "white", borderRadius: 16, padding: 16, boxShadow: "0 10px 30px rgba(0,0,0,0.08)", height: "calc(100vh - 40px)", overflow: "auto" }}>
          <h3 style={{ marginTop: 0, color: "#555" }}>Recent History</h3>
          <button onClick={refreshRuns} style={{ width: "100%", padding: 10, borderRadius: 12, border: "1px solid #000", background: "white", fontWeight: 700, color: "#555", cursor: "pointer" }}>
            Refresh
          </button>

          <div style={{ marginTop: 12, display: "grid", gap: 10 }}>
            {runs.map(r => (
              <div
                key={r.id}
                onClick={() => openRun(r.id)}
                style={{
                  border: "1px solid #eee",
                  borderRadius: 12,
                  padding: 12,
                  cursor: "pointer",
                  background: activeRun?.id === r.id ? "#f3f6ff" : "white",
                  color: activeRun?.id === r.id ? "#000" : "#333",
                }}
              >
                <div style={{ fontWeight: 800, fontSize: 13 }}>{r.mode}</div>
                <div style={{ fontSize: 12, color: "#555", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                  {r.input_text}
                </div>
                <div style={{ marginTop: 6, fontSize: 12, color: "#555" }}><b>Status:</b> {r.status}</div>
                <div style={{ marginTop: 6, fontSize: 12, color: "#555" }}>
                  <b>Privacy:</b>{" "}
                  {r.no_store ? "No-store" : r.pii_detected ? `PII (${r.pii_summary || "detected"})` : "Normal"}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* RIGHT */}
        <div style={{ background: "white", borderRadius: 16, padding: 18, boxShadow: "0 10px 30px rgba(0,0,0,0.08)" }}>
          <h2 style={{ margin: 0, color: "#555" }}>Stratigus Private AI Agent</h2>
          <p style={{ marginTop: 6, color: "#555" }}>Local-first inference (LM Studio) with privacy mode and run history.</p>

          <div style={{ display: "grid", gap: 10, marginTop: 14 }}>
            <label style={{ fontWeight: 800 }}>Enter URL / Question</label>
            <textarea
              rows={3}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="https://example.com"
              style={{ padding: 12, borderRadius: 12, border: "1px solid #d9dbe3" }}
            />

            <div style={{ display: "flex", gap: 12, flexWrap: "wrap", alignItems: "center" }}>
              <div style={{ flex: "1 1 240px" }}>
                <label style={{ fontWeight: 800, color: "#555" }}>Choose Option</label>
                <select
                  value={mode}
                  onChange={(e) => setMode(e.target.value)}
                  style={{ width: "100%", padding: 10, borderRadius: 12, border: "1px solid #d9dbe3" }}
                >
                  {MODES.map(m => <option key={m} value={m}>{m}</option>)}
                </select>
              </div>

              <button
                onClick={onRun}
                disabled={loading || !input.trim()}
                style={{
                  flex: "1 1 200px",
                  padding: "12px 16px",
                  borderRadius: 12,
                  border: "1px solid #1f2430",
                  background: loading ? "#f0f1f4" : "white",
                  color: "#1f2430",
                  hover: { background: loading ? "#f0f1f4" : "#555" },
                  fontWeight: 900,
                  cursor: loading ? "not-allowed" : "pointer"
                }}
              >
                {loading ? "Running..." : "Create & Send"}
              </button>
            </div>

            {/* Privacy toggles */}
            <div style={{ display: "grid", gap: 8, color: "#555" }}>
              <label style={{ display: "flex", gap: 10, alignItems: "center" }}>
                <input type="checkbox" checked={noStore} onChange={(e) => setNoStore(e.target.checked)} />
                <span><b>Do not save this run</b></span>
              </label>

              <label style={{ display: "flex", gap: 10, alignItems: "center" }}>
                <input
                  type="checkbox"
                  checked={redactBeforeStore}
                  onChange={(e) => setRedactBeforeStore(e.target.checked)}
                  disabled={noStore}
                  style={{ background: "#fff" }}
                />
                <span><b>Redact detected personal data</b> before saving</span>
              </label>

              <div style={{ fontSize: 12, color: "#666" }}>
                Privacy notice: avoid submitting personal/sensitive data unless you have permission.
              </div>
            </div>

            {error && (
              <div style={{ padding: 12, borderRadius: 12, border: "1px solid #ffb3b3", background: "#fff5f5" }}>
                <b>Error:</b> {error}
              </div>
            )}

            <h3 style={{ marginBottom: 6, color: "#555" }}>Run Details</h3>
            {!activeRun ? (
              <div style={{ color: "#666" }}>Select a run from the history list.</div>
            ) : (
              <div style={{ display: "grid", gap: 10, color: "#555" }}>
                <div><b>ID:</b> {activeRun.id}</div>
                <div><b>Status:</b> {activeRun.status}</div>
                <div><b>Mode:</b> {activeRun.mode}</div>

                {activeRun.error && (
                  <div style={{ padding: 12, borderRadius: 12, border: "1px solid #ffb3b3", background: "#fff5f5", color: "#555" }}>
                    <b>Backend Error:</b> {activeRun.error}
                  </div>
                )}

                <label style={{ fontWeight: 800 }}>Output</label>
                <pre style={{ padding: 14, borderRadius: 12, border: "1px solid #e3e5ee", background: "#fafbff", whiteSpace: "pre-wrap", wordBreak: "break-word", minHeight: 220, color: "#555" }}>
                  {activeRun.result || "—"}
                </pre>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
