import { useState } from "react";
import { analyse } from "./api";

const MODES = ["Summarise", "Key Points", "Security Analysis", "Free"];

export default function App() {
  const [input, setInput] = useState("");
  const [mode, setMode] = useState(MODES[0]);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState("");
  const [error, setError] = useState("");

  async function onRun() {
    setError("");
    setResult("");
    setLoading(true);
    try {
      const out = await analyse({ input, mode });
      setResult(out);
    } catch (e) {
      setError(e.message || String(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ minHeight: "100vh", background: "#f6f7fb", padding: 30 }}>
      <div style={{
        maxWidth: 980, margin: "0 auto", background: "white",
        borderRadius: 16, padding: 22, boxShadow: "0 10px 30px rgba(0,0,0,0.08)",
        fontFamily: "Arial"
      }}>
        <h1 style={{ margin: 0 }}>Private AI Web Analysis Agent</h1>
        <p style={{ marginTop: 6, color: "#555" }}>
          React UI → Flask API → LM Studio local model (with tool-based webpage fetching)
        </p>

        <div style={{ display: "grid", gap: 10, marginTop: 14 }}>
          <label style={{ fontWeight: 700 }}>URL or Question</label>
          <textarea
            rows={3}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Example: Summarise https://example.com"
            style={{
              padding: 12, borderRadius: 12, border: "1px solid #d9dbe3",
              outline: "none", fontSize: 14
            }}
          />

          <div style={{ display: "flex", gap: 12, alignItems: "center" }}>
            <div style={{ display: "grid", gap: 6 }}>
              <label style={{ fontWeight: 700 }}>Mode</label>
              <select
                value={mode}
                onChange={(e) => setMode(e.target.value)}
                style={{
                  padding: 10, borderRadius: 12, border: "1px solid #d9dbe3",
                  fontSize: 14, width: 220
                }}
              >
                {MODES.map((m) => <option key={m} value={m}>{m}</option>)}
              </select>
            </div>

            <button
              onClick={onRun}
              disabled={loading || !input.trim()}
              style={{
                marginLeft: "auto",
                padding: "12px 16px",
                borderRadius: 12,
                border: "1px solid #1f2430",
                background: loading ? "#f0f1f4" : "white",
                cursor: loading ? "not-allowed" : "pointer",
                fontWeight: 800
              }}
            >
              {loading ? "Running..." : "Analyse"}
            </button>
          </div>

          {error && (
            <div style={{
              padding: 12, borderRadius: 12, border: "1px solid #ffb3b3",
              background: "#fff5f5"
            }}>
              <b>Error:</b> {error}
            </div>
          )}

          <label style={{ fontWeight: 700, marginTop: 6 }}>Output</label>
          <pre style={{
            padding: 14, borderRadius: 12, border: "1px solid #e3e5ee",
            background: "#fafbff", whiteSpace: "pre-wrap", minHeight: 180
          }}>
            {result || (loading ? "Processing..." : "—")}
          </pre>
        </div>
      </div>
    </div>
  );
}
