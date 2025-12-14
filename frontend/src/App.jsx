import { useState } from "react";
import { analyse } from "./api";

const MODES = ["Summarise", "Key Points", "Security Analysis", "All"];

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
    <div style={{
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      minHeight: "100vh",
      width: "100vw",
      background: "#555",
      boxSizing: "border-box",
      padding: 30
    }}>
      <div style={{
        minHeight: "100vh",
        width: "100%",
        // maxWidth: "1200px",
        padding: "24px",
        boxSizing: "border-box",
        background: "white",
        borderRadius: "16px",
        boxShadow: "0 10px 30px rgba(0,0,0,0.08)",
      }}>
        <h2 style={{ margin: 0, color: "#555" }}>Stratigus Private AI Agent</h2>
        <p style={{ marginTop: 6, color: "#555" }}>
          LM Studio local model (with tool-based webpage fetching)
        </p>

        <div style={{ display: "grid", gap: 10, marginTop: 14 }}>
          <label style={{ fontWeight: 700, color: "#555" }}>Enter URL or Question</label>
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
              <label style={{ fontWeight: 700, color: "#555" }}>Choose Mode(Optional)</label>
              <select
                value={mode}
                onChange={(e) => setMode(e.target.value)}
                style={{
                  padding: 10, borderRadius: 12, border: "1px solid #d9dbe3ff",
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
                background: loading ? "#121314ff" : "#1f2430",
                color: "white",
                cursor: loading ? "not-allowed" : "pointer",
                fontWeight: 500
              }}
            >
              {loading ? "Running..." : "Send"}
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
            background: "#000", whiteSpace: "pre-wrap", minHeight: 180
          }}>
            {result || (loading ? "Processing..." : "—")}
          </pre>
        </div>
      </div>
    </div>
  );
}
