# 0/1 Knapsack Dynamic Programming Laboratory

A high-precision, interactive algorithmic workbench and simulation environment for analyzing the classic **0/1 Knapsack Problem** via bottom-up Dynamic Programming. Designed for BCA Semester 6 **Design and Analysis of Algorithms (DAA)** coursework, lab practicals, and theoretical examination prep.

---

## Overview

The 0/1 Knapsack problem is a foundational problem in combinatorial optimization and dynamic programming. This application bridges theoretical algorithm analysis and interactive execution by providing:

1. **Step-by-Step DP Matrix Visualization:** Inspect subproblem evaluations cell-by-cell with color-coded dependency tracing (Target Cell, Exclude Reference, Include Reference, and Optimal Traceback Path).
2. **Branch Decision Diagnostics:** Live mathematical breakdown of the Bellman recurrence relation for every subproblem coordinate $(i, j)$.
3. **Traceback Reconstruction:** Step-by-step path recovery demonstrating how the optimal subset of items is extracted from the completed matrix.
4. **Greedy vs. DP Benchmarking:** Concrete counterexample demonstrations showing why the value-to-weight density greedy heuristic fails for indivisible items.
5. **Multi-Language Lab Implementations:** Standard, production-grade implementations in Python 3, C++ (STL), Java, and ANSI C.
6. **Academic Reference Suite:** CLRS textbook pseudocode, 1D array space-optimization derivation ($\mathcal{O}(W)$ space), pseudo-polynomial complexity proofs, and viva/exam question banks.

---

## Algorithmic Foundation

### Problem Statement
Given $n$ items, each with a positive integer weight $w_i$ and value $v_i$, and a knapsack of maximum weight capacity $W$, determine binary decision variables $x_i \in \{0, 1\}$ to maximize total value while respecting total capacity:

$$\max \sum_{i=1}^n v_i x_i \quad \text{subject to} \quad \sum_{i=1}^n w_i x_i \le W$$

### Bellman Recurrence Equation
Let $DP[i, j]$ denote the maximum value obtainable using a subset of the first $i$ candidate items ($0 \le i \le n$) under capacity constraint $j$ ($0 \le j \le W$):

$$DP[i, j] = 
\begin{cases} 
  0 & \text{if } i = 0 \text{ or } j = 0 \\
  DP[i - 1, j] & \text{if } w_i > j \\
  \max\Big( DP[i - 1, j], \; v_i + DP[i - 1, j - w_i] \Big) & \text{if } w_i \le j
\end{cases}$$

### Complexity Profile

| Metric | Bound | Theoretical Classification |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(n \cdot W)$ | Pseudo-polynomial time (dependent on numeric value $W$) |
| **Space Complexity (2D)** | $\mathcal{O}(n \cdot W)$ | Required for full item subset reconstruction via traceback |
| **Space Complexity (1D)** | $\mathcal{O}(W)$ | Optimized space when only the optimal value is needed |
| **Traceback Time** | $\mathcal{O}(n)$ | Path recovery from $(n, W)$ back to row 0 |

---

## Laboratory Features

### 1. Interactive Execution Engine
- **Preset Configurations:** Built-in standard DAA instances, textbook benchmarks, and greedy counterexample datasets.
- **Custom Input Vectors:** Support for custom weights, values, and knapsack capacity configurations.
- **Transport Controls:** Step forward, step backward, jump to start/end, and auto-play with adjustable playback speed (0.15s, 0.5s, 1.0s).
- **Timeline Scrubber:** Jump directly to any phase of matrix construction or backtracking.

### 2. High-Contrast DP Matrix Renderer
- Clear, matrix-style tabular display with frozen row/column labels and item metadata (weight, value, density ratio $v_i / w_i$).
- Distinct visual states:
  - `Target Cell`: Active subproblem coordinate $(i, j)$ currently being evaluated.
  - `Exclude Reference`: Reference value from $DP[i-1, j]$.
  - `Include Reference`: Reference value from $DP[i-1, j - w_i]$.
  - `Optimal Traceback Path`: Highlighted path traversed during solution reconstruction.

### 3. Comprehensive Academic Curriculum
- **Mathematical Foundations:** Formal proofs of Optimal Substructure and Overlapping Subproblems.
- **Greedy Analysis Tab:** Side-by-side metric comparison, optimality gap calculation, and item-density ranking table.
- **Code Reference Tab:** Clean lab-ready code with memory-efficient traceback logic for Python, C++, Java, and C.
- **Viva & Exam Guide:** Key answers covering Fractional vs. 0/1 Knapsack, Unbounded Knapsack comparisons, and exam summary tables.
- **1D Space Optimization:** Explanation of why backward iteration ($j = W \dots w_i$) is mandatory to prevent unbounded item reuse.

---

## Project Structure

```text
Knapsack Simulator/
├── app.py              # Main Streamlit application (engine, renderer, UI, learning suite)
├── requirements.txt    # Python package dependencies
└── README.md           # Laboratory documentation and algorithmic reference
```

---

## Installation & Running Locally

### Prerequisites
- Python 3.8 or higher installed on your system.

### 1. Clone or Navigate to Directory
```bash
cd "d:/BCA/Semester/Semester 6/DAA/Knapsack Simulator"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Simulator
```bash
streamlit run app.py
```

Once launched, Streamlit will automatically open the application in your default web browser (typically at `http://localhost:8501`).

---

## Technology Stack

- **Framework:** Streamlit (Python)
- **Mathematical Typesetting:** KaTeX / LaTeX
- **Layout & Styling:** Clean, high-contrast custom CSS with responsive card grids and theme-aware styling.
