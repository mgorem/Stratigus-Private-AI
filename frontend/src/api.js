export async function analyse({ input, mode }) {
    const res = await fetch(
        import.meta.env.VITE_API_URL + "/api/analyse",
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ input, mode }),
        }
    );

    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Request failed");
    return data.result;
}
