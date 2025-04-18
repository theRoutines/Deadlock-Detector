# Deadlock-Detector 🛠️

A comprehensive deadlock detection and resolution tool that implements both graphical (Resource Allocation Graph) and matrix-based detection algorithms. This tool provides an intuitive GUI interface for modeling, detecting, and resolving deadlocks in concurrent systems.

## Features ✨

- **Dual Detection Methods**
  - Resource Allocation Graph (RAG) visualization
  - Matrix-based deadlock detection algorithm
  - Real-time cycle detection in directed graphs
  - Process and resource state tracking

- **Interactive GUI**
  - Modern and intuitive interface
  - Visual representation of system state
  - Color-coded processes and resources
  - Real-time feedback on system changes

- **Deadlock Resolution**
  - Automatic detection of circular wait chains
  - Smart resolution suggestions
  - Multiple recovery strategies
  - Resource preemption recommendations

- **System Modeling**
  - Add/remove processes and resources
  - Create allocation and request edges
  - Track resource availability
  - Monitor system state changes

## Implementation Details 🔧

The project implements two main approaches to deadlock detection:

1. **Resource Allocation Graph (RAG) Method**
   - Uses NetworkX for graph operations
   - Visualizes processes and resources as nodes
   - Represents allocations and requests as directed edges
   - Detects cycles in the directed graph

2. **Matrix-Based Detection**
   - Implements the Banker's Algorithm
   - Maintains allocation and request matrices
   - Tracks available resources
   - Uses marking algorithm for deadlock detection

## Requirements 📋

- Python 3.x
- Required Python packages:
  - tkinter (usually comes with Python)
  - networkx
  - matplotlib

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/theRoutines/Deadlock-Detector.git
cd Deadlock-Detector
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv env

# On Windows:
.\env\Scripts\activate

# On Unix or MacOS:
source env/bin/activate
```

3. Install required packages:
```bash
pip install networkx matplotlib
```

## Usage 🖥️

1. Run the GUI application:
```bash
python main6.py
```

2. Using the tool:
   - Add processes and resources using the respective buttons
   - Create allocations and requests between processes and resources
   - Click "Detect Deadlock" to check for deadlocks
   - Use "Visualize RAG" to see the current system state
   - Follow resolution suggestions if a deadlock is detected
   - Use "Refresh" to clear the system and start fresh

## Example Scenario 📝

1. Add two processes (P1, P2) and two resources (R1, R2)
2. Allocate R1 to P1 and R2 to P2
3. Create request from P1 to R2
4. Create request from P2 to R1
5. Click "Detect Deadlock" to identify the circular wait
6. Follow the suggested resolution steps

## Code Structure 📁

- `main6.py`: Main GUI application with RAG implementation
- `git.py`: Matrix-based deadlock detection implementation
- Other main files contain different versions and implementations

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- NetworkX for graph operations
- Matplotlib for visualization
- Tkinter for the GUI framework 
