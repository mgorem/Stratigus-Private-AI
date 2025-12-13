# gui_app_enhanced.py
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
from backend.agent_app import run_agent

MODES = [
    "Summarise page",
    "Security risk analysis",
    "Key points only",
    "Free question"
]


def build_prompt(user_text: str, mode: str) -> str:
    if mode == "Summarise page":
        return f"Please fetch and summarise the main ideas from this page:\n{user_text}"
    elif mode == "Security risk analysis":
        return f"Fetch the page and analyse any security and privacy risks:\n{user_text}"
    elif mode == "Key points only":
        return f"Fetch this page and list only the key bullet points:\n{user_text}"
    else:  # Free question
        return user_text


def log(message: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_box.insert(tk.END, f"[{ts}] {message}\n")
    log_box.see(tk.END)


def on_analyse_click():
    raw_input = url_entry.get().strip()
    mode = mode_var.get()

    if not raw_input:
        messagebox.showwarning("Input required", "Please enter a URL or question.")
        return

    final_prompt = build_prompt(raw_input, mode)

    analyse_button.config(state=tk.DISABLED)
    status_label.config(text="Status: Running...")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Analysing... please wait.\n")
    log(f"Started analysis | Mode: {mode} | Input: {raw_input}")

    try:
        answer = run_agent(final_prompt)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, answer)
        status_label.config(text="Status: Done")
        log("Analysis completed successfully.")
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {e}")
        status_label.config(text="Status: Error")
        log(f"Error during analysis: {e}")
    finally:
        analyse_button.config(state=tk.NORMAL)


# GUI setup
root = tk.Tk()
root.title("Private AI Web Analysis Agent")

tk.Label(root, text="Enter URL or question about a webpage:").pack(pady=(10, 0))
url_entry = tk.Entry(root, width=80)
url_entry.pack(padx=10, pady=5)

# Mode dropdown
tk.Label(root, text="Select analysis mode:").pack()
mode_var = tk.StringVar(value=MODES[0])
mode_menu = tk.OptionMenu(root, mode_var, *MODES)
mode_menu.pack(pady=(0, 10))

analyse_button = tk.Button(root, text="Analyse Web Page", command=on_analyse_click)
analyse_button.pack(pady=5)

status_label = tk.Label(root, text="Status: Idle")
status_label.pack(pady=(0, 5))

tk.Label(root, text="Agent Response:").pack(pady=(10, 0))
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=18)
output_box.pack(padx=10, pady=5)

tk.Label(root, text="Log:").pack(pady=(10, 0))
log_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=10)
log_box.pack(padx=10, pady=(0, 10))

root.mainloop()
