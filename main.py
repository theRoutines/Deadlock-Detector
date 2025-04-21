import tkinter as tk
from tkinter import messagebox, simpledialog
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Global graph for processes and resources
G = nx.DiGraph()

# Function to add a process node
def add_process():
    pid = simpledialog.askstring("Process ID", "Enter Process ID (e.g., P1):")
    if pid:
        G.add_node(pid, type='process')
        messagebox.showinfo("Success", f"Process {pid} added.")

# Function to add a resource node
def add_resource():
    rid = simpledialog.askstring("Resource ID", "Enter Resource ID (e.g., R1):")
    if rid:
        G.add_node(rid, type='resource')
        messagebox.showinfo("Success", f"Resource {rid} added.")

# Function to add an allocation edge (Resource -> Process)
def allocate_resource():
    rid = simpledialog.askstring("Resource ID", "Enter Resource ID to allocate:")
    pid = simpledialog.askstring("Process ID", "Enter Process ID receiving resource:")
    if rid and pid:
        G.add_edge(rid, pid)
        messagebox.showinfo("Success", f"Resource {rid} allocated to {pid}.")

# Function to add a request edge (Process -> Resource)
def request_resource():
    pid = simpledialog.askstring("Process ID", "Enter Process ID requesting resource:")
    rid = simpledialog.askstring("Resource ID", "Enter Resource ID being requested:")
    if pid and rid:
        G.add_edge(pid, rid)
        messagebox.showinfo("Success", f"{pid} requests {rid}.")

# Function to detect deadlocks (cycle in Resource Allocation Graph)
def detect_deadlock():
    try:
        cycle = nx.find_cycle(G, orientation='original')
        deadlock_message = "Deadlock detected!\nCircular wait chain:\n"
        for u, v, _ in cycle:
            deadlock_message += f"{u} → {v}\n"
        messagebox.showerror("Deadlock Detected", deadlock_message)
    except nx.NetworkXNoCycle:
        messagebox.showinfo("Safe State", "No Deadlock detected. System is safe.")

# Function to visualize the Resource Allocation Graph
def visualize_graph():
    pos = nx.spring_layout(G)
    process_nodes = [n for n, attr in G.nodes(data=True) if attr['type'] == 'process']
    resource_nodes = [n for n, attr in G.nodes(data=True) if attr['type'] == 'resource']

    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, nodelist=process_nodes, node_color='skyblue', node_size=700, label='Processes')
    nx.draw_networkx_nodes(G, pos, nodelist=resource_nodes, node_color='lightgreen', node_size=700, label='Resources')
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    plt.title("Resource Allocation Graph (RAG)")
    plt.legend(scatterpoints=1)
    plt.axis('off')
    plt.show()

# GUI setup
root = tk.Tk()
root.title("Automated Deadlock Detection Tool")
root.geometry("400x450")

tk.Label(root, text="Deadlock Detection Tool", font=("Helvetica", 16, "bold")).pack(pady=20)

tk.Button(root, text="Add Process", command=add_process, width=25, height=2, bg="#add8e6").pack(pady=5)
tk.Button(root, text="Add Resource", command=add_resource, width=25, height=2, bg="#90ee90").pack(pady=5)
tk.Button(root, text="Allocate Resource", command=allocate_resource, width=25, height=2, bg="#ffd700").pack(pady=5)
tk.Button(root, text="Request Resource", command=request_resource, width=25, height=2, bg="#ffa07a").pack(pady=5)
tk.Button(root, text="Detect Deadlock", command=detect_deadlock, width=25, height=2, bg="#ff6347").pack(pady=5)
tk.Button(root, text="Visualize RAG", command=visualize_graph, width=25, height=2, bg="#d3d3d3").pack(pady=5)

tk.Button(root, text="Exit", command=root.quit, width=25, height=2, bg="#c0c0c0").pack(pady=20)

root.mainloop()
