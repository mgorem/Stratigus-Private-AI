import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests

API_URL = "http://localhost:5000/api/analyse"

def analyse():
    user_text = input_box.get().strip()
    mode = mode_var.get()

    if not user_text:
        messagebox.showwarning("Input required", "Enter a URL or question.")
        return

    run_btn.config(state=tk.DISABLED)
    status_label.config(text="Status: Running...")
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Processing...\n")

    try:
        r = requests.post(API_URL, json={"input": user_text, "mode": mode}, timeout=300)
        data = r.json()
        if r.status_code != 200:
            raise Exception(data.get("error", "Unknown error"))
        output.delete("1.0", tk.END)
        output.insert(tk.END, data["result"])
        status_label.config(text="Status: Done")
    except Exception as e:
        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Error: {e}")
        status_label.config(text="Status: Error")
    finally:
        run_btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Stratigus Private AI Agent (Desktop)")

tk.Label(root, text="URL / Question").pack(pady=(10, 0))
input_box = tk.Entry(root, width=90)
input_box.pack(padx=10, pady=5)

tk.Label(root, text="Mode").pack()
mode_var = tk.StringVar(value="Summarise")
modes = ["Summarise", "Key Points", "Security Analysis", "All"]
mode_menu = tk.OptionMenu(root, mode_var, *modes)
mode_menu.pack(pady=(0, 10))

run_btn = tk.Button(root, text="Analyse", command=analyse)
run_btn.pack()

status_label = tk.Label(root, text="Status: Idle")
status_label.pack(pady=(5, 10))

output = scrolledtext.ScrolledText(root, width=110, height=25, wrap=tk.WORD)
output.pack(padx=10, pady=(0, 10))

root.mainloop()
