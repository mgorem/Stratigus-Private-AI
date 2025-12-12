# gui_app.py
import tkinter as tk
from tkinter import scrolledtext, messagebox
from agent_app import run_agent  # uses LM Studio + fetch_webpage


def on_analyse_click():
    user_text = url_entry.get().strip()
    if not user_text:
        messagebox.showwarning("Input required", "Please enter a URL or question.")
        return

    analyse_button.config(state=tk.DISABLED)
    status_label.config(text="Status: Running...")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Analysing... please wait.\n")

    try:
        answer = run_agent(user_text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, answer)
        status_label.config(text="Status: Done")
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {e}")
        status_label.config(text="Status: Error")
    finally:
        analyse_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Stratigus | Private AI Agent")

tk.Label(root, text="Enter URL or question about a webpage:").pack(pady=(10, 0))

url_entry = tk.Entry(root, width=80)
url_entry.pack(padx=10, pady=5)

analyse_button = tk.Button(root, text="Analyse Web Page", command=on_analyse_click)
analyse_button.pack(pady=5)

status_label = tk.Label(root, text="Status: Idle")
status_label.pack(pady=(0, 5))

tk.Label(root, text="Agent Response:").pack(pady=(10, 0))
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=25)
output_box.pack(padx=10, pady=5)

root.mainloop()
