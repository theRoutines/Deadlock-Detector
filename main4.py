import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


G = nx.DiGraph()


def show_custom_message(title, message, bg_color="#ffffff"):
    win = tk.Toplevel()
    win.title(title)
    win.geometry("350x200")
    win.configure(bg=bg_color)
    win.resizable(False, False)
    tk.Label(win, text=title, font=("Helvetica", 16, "bold"), bg=bg_color, fg="#333").pack(pady=10)
    text_frame = tk.Frame(win, bg=bg_color)
    text_frame.pack(pady=5)
    tk.Message(text_frame, text=message, font=("Helvetica", 12), bg=bg_color, width=350).pack()
    ttk.Button(win, text="OK", command=win.destroy).pack(pady=20)
    win.grab_set()

# Override the simpledialog to make it wider
def wide_askstring(title, prompt):
    # Create a custom dialog that's wider than the default simpledialog
    dialog = tk.Toplevel()
    dialog.title(title)
    dialog.geometry("350x150")
    dialog.resizable(False, False)
    
    # Center the dialog
    dialog.update_idletasks()
    width = dialog.winfo_width()
    height = dialog.winfo_height()
    x = (dialog.winfo_screenwidth() // 2) - (width // 2)
    y = (dialog.winfo_screenheight() // 2) - (height // 2)
    dialog.geometry(f'{width}x{height}+{x}+{y}')
    
    # Add content
    tk.Label(dialog, text=prompt, font=("Helvetica", 12)).pack(pady=10)
    entry = ttk.Entry(dialog, width=30)
    entry.pack(pady=10)
    entry.focus_set()
    
    result = [None]
    
    def on_ok():
        result[0] = entry.get()
        dialog.destroy()
    
    def on_cancel():
        dialog.destroy()
    
    # Buttons
    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=10)
    ttk.Button(button_frame, text="OK", command=on_ok).pack(side="left", padx=10)
    ttk.Button(button_frame, text="Cancel", command=on_cancel).pack(side="left", padx=10)
    
    # Make dialog modal
    dialog.transient(dialog.master)
    dialog.grab_set()
    
    # Wait for dialog to close
    dialog.wait_window()
    return result[0]

def add_process():
    pid = wide_askstring("Add Process", "Enter Process ID (e.g., P1):")
    if pid:
        G.add_node(pid, type='process')
        show_custom_message("Process Added", f"Process {pid} added successfully!", "#d9faff")

def add_resource():
    rid = wide_askstring("Add Resource", "Enter Resource ID (e.g., R1):")
    if rid:
        G.add_node(rid, type='resource')
        show_custom_message("Resource Added", f"Resource {rid} added successfully!", "#e7ffd9")

def allocate_resource():
    rid = wide_askstring("Allocate Resource", "Enter Resource ID to allocate:")
    if rid:
        pid = wide_askstring("Allocate Resource", "Enter Process ID receiving the resource:")
        if pid:
            G.add_edge(rid, pid)
            show_custom_message("Allocation Successful", f"Resource {rid} allocated to {pid}.", "#fff8dc")

def request_resource():
    pid = wide_askstring("Request Resource", "Enter Process ID requesting the resource:")
    if pid:
        rid = wide_askstring("Request Resource", "Enter Resource ID being requested:")
        if rid:
            G.add_edge(pid, rid)
            show_custom_message("Request Added", f"{pid} is requesting {rid}.", "#ffebd9")

def detect_deadlock():
    try:
        cycle = nx.find_cycle(G, orientation='original')
        deadlock_message = "⚠️ Deadlock detected!\n\nCircular wait chain:\n"
        for u, v, _ in cycle:
            deadlock_message += f"{u} → {v}\n"
        show_custom_message("Deadlock Detected", deadlock_message, "#ffe6e6")

        suggest_resolutions(cycle)

    except nx.NetworkXNoCycle:
        show_custom_message("Safe State", "✅ No Deadlock detected. System is safe.", "#d9ffd9")

def suggest_resolutions(cycle):
    res_message = "💡 Possible Deadlock Resolutions:\n\n"
    res_message += "1️⃣ Terminate one of the processes in the cycle.\n"
    res_message += "2️⃣ Preempt resources held by a process and allocate to waiting ones.\n"
    res_message += "3️⃣ Rollback one or more processes to break the circular wait.\n"
    res_message += "4️⃣ Modify resource allocation policies to avoid circular wait.\n\n"
    res_message += "📝 Suggested Action: Preempt resource from one of the following resources to break the cycle:\n"

    resources_in_cycle = [u for u, v, _ in cycle if G.nodes[u].get('type') == 'resource']
    if resources_in_cycle:
        res_message += ", ".join(resources_in_cycle)
    else:
        res_message += "No resources directly involved."

    show_custom_message("Resolution Suggestions", res_message, "#f0f0f0")

def visualize_graph():
    pos = nx.spring_layout(G, seed=42)
    process_nodes = [n for n, attr in G.nodes(data=True) if attr.get('type') == 'process']
    resource_nodes = [n for n, attr in G.nodes(data=True) if attr.get('type') == 'resource']

    plt.figure(figsize=(9, 7))
    nx.draw_networkx_nodes(G, pos, nodelist=process_nodes, node_color='#87ceeb', node_size=800, label='Processes')
    nx.draw_networkx_nodes(G, pos, nodelist=resource_nodes, node_color='#90ee90', node_size=800, label='Resources')
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=25, edge_color='#444')
    nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

    plt.title("Resource Allocation Graph (RAG)", fontsize=18, fontweight='bold')
    plt.legend(["Processes", "Resources"], loc='upper left')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def refresh_graph():
    G.clear()
    show_custom_message("System Refreshed", "All entries and connections have been cleared.\nYou can now start fresh!", "#f9f9f9")

# Main window setup
root = tk.Tk()
root.title("Automated Deadlock Detection Tool")
root.geometry("450x600")
root.configure(bg="#f0f8ff")

# Header
tk.Label(root, text="💻 Deadlock Detection Tool", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#333").pack(pady=25)

# Themed buttons with modern spacing
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10)

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

buttons = [
    ("➕ Add Process", add_process, "#add8e6"),
    ("➕ Add Resource", add_resource, "#90ee90"),
    ("🔄 Allocate Resource", allocate_resource, "#ffe680"),
    ("📥 Request Resource", request_resource, "#ffb380"),
    ("⚠️ Detect Deadlock", detect_deadlock, "#ff6666"),
    ("📊 Visualize RAG", visualize_graph, "#d3d3d3"),
    ("🧹 Refresh (Clear All)", refresh_graph, "#c0c0c0"),
    ("🚪 Exit", root.quit, "#e0e0e0")
]

for text, command, color in buttons:
    btn = tk.Button(button_frame, text=text, command=command, width=30, height=2, bg=color, fg="#333", font=("Helvetica", 13, "bold"), relief="raised", bd=2)
    btn.pack(pady=8)

root.mainloop()
