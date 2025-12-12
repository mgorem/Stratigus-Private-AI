# gui_app.py
import tkinter as tk
from tkinter import scrolledtext, messagebox
from agent_app import run_agent


def on_analyse_click():
    user_text = url_entry.get().strip()
    if not user_text:
        messagebox.showwarning("Input required", "Please enter a URL or question.")
        return

    # Disable button while processing
    analyse_button.config(state=tk.DISABLED)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Analysing... please wait.\n")

    try:
        answer = run_agent(user_text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, answer)
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {e}")
    finally:
        analyse_button.config(state=tk.NORMAL)


# Create main window
root = tk.Tk()
root.title("Private AI Web Analysis Agent")

# URL / question label + entry
tk.Label(root, text="Enter URL or question about a webpage:").pack(pady=(10, 0))

url_entry = tk.Entry(root, width=80)
url_entry.pack(padx=10, pady=5)

# Analyse button
analyse_button = tk.Button(root, text="Analyse Web Page", command=on_analyse_click)
analyse_button.pack(pady=5)

# Output area
tk.Label(root, text="Agent Response:").pack(pady=(10, 0))

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=25)
output_box.pack(padx=10, pady=5)

# Start GUI loop
root.mainloop()
