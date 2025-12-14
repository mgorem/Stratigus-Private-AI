const API = import.meta.env.VITE_API_URL || "http://localhost:5000";

export async function createRun(payload) {
    const res = await fetch(`${API}/api/runs`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    });
    const data = await res.json();

    if (res.status === 409) return { requires_confirmation: true, ...data };
    if (!res.ok) throw new Error(data.error || "Failed to create run");
    return data;
}

export async function executeRun(runId) {
    const res = await fetch(`${API}/api/runs/${runId}/execute`, { method: "POST" });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Failed to execute run");
    return data;
}

export async function getRun(runId) {
    const res = await fetch(`${API}/api/runs/${runId}`);
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Failed to fetch run");
    return data;
}

export async function listRuns() {
    const res = await fetch(`${API}/api/runs`);
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Failed to list runs");
    return data;
}
