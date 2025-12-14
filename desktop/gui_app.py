import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
import os

API_BASE = os.getenv("API_BASE", "http://localhost:5000")


def create_and_execute():
    user_text = input_box.get().strip()
    mode = mode_var.get()
    no_store = bool(no_store_var.get())
    redact = bool(redact_var.get())

    if not user_text:
        messagebox.showwarning("Input required", "Enter a URL or question.")
        return

    run_btn.config(state=tk.DISABLED)
    status_label.config(text="Status: Creating run...")
    output.delete("1.0", tk.END)

    payload = {
        "input": user_text,
        "mode": mode,
        "no_store": no_store,
        "redact_before_store": redact,
        "require_confirm_if_pii": True,
        "confirmed_pii": False
    }

    try:
        r = requests.post(f"{API_BASE}/api/runs", json=payload, timeout=60)
        data = r.json()

        if r.status_code == 409 and data.get("requires_confirmation"):
            findings = data.get("findings", [])
            details = "\n".join([f"- {f['kind']}: {f['sample']}" for f in findings]) or "(none shown)"

            ok = messagebox.askyesno(
                "Privacy warning",
                f"{data.get('message')}\n\nDetected:\n{details}\n\nProceed?"
            )
            if not ok:
                status_label.config(text="Status: Cancelled by user")
                run_btn.config(state=tk.NORMAL)
                return

            payload["confirmed_pii"] = True
            r = requests.post(f"{API_BASE}/api/runs", json=payload, timeout=60)
            data = r.json()

        if r.status_code not in (200, 201):
            raise Exception(data.get("error", "Failed to create run"))

        run_id = data["run_id"]

        status_label.config(text=f"Status: Executing run {run_id} ...")
        r2 = requests.post(f"{API_BASE}/api/runs/{run_id}/execute", timeout=300)
        data2 = r2.json()

        if r2.status_code != 200:
            raise Exception(data2.get("error", "Execution failed"))

        # If no_store, result may be returned directly
        if "result" in data2 and data2["result"]:
            result_text = data2["result"]
        else:
            r3 = requests.get(f"{API_BASE}/api/runs/{run_id}", timeout=60)
            data3 = r3.json()
            result_text = data3.get("result", "")

        output.insert(tk.END, result_text or "—")
        status_label.config(text="Status: Done")

    except Exception as e:
        output.insert(tk.END, f"Error: {e}")
        status_label.config(text="Status: Error")
    finally:
        run_btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Stratigus Private AI Agent (Desktop)")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="URL / Question").pack(anchor="w")
input_box = tk.Entry(frame, width=100)
input_box.pack(fill="x", pady=5)

tk.Label(frame, text="Mode").pack(anchor="w")
mode_var = tk.StringVar(value="Summarise")
mode_menu = tk.OptionMenu(frame, mode_var, "Summarise", "Key Points", "Security Analysis", "Free")
mode_menu.pack(anchor="w", pady=(0, 10))

no_store_var = tk.IntVar(value=0)
redact_var = tk.IntVar(value=1)

tk.Checkbutton(frame, text="Do not save this run (ephemeral)", variable=no_store_var).pack(anchor="w")
tk.Checkbutton(frame, text="Redact personal data before saving", variable=redact_var).pack(anchor="w", pady=(0,10))

run_btn = tk.Button(frame, text="Create & Execute Run", command=create_and_execute)
run_btn.pack(fill="x")

status_label = tk.Label(frame, text="Status: Idle")
status_label.pack(anchor="w", pady=(8, 8))

output = scrolledtext.ScrolledText(frame, width=120, height=25, wrap=tk.WORD)
output.pack(fill="both", expand=True)

root.mainloop()
