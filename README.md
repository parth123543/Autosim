# AUTOSIM: Mealy &harr; Moore Automata Simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing%20(100%25)-success.svg)](python_core/test_converter.py)
[![Zero Dependency Web App](https://img.shields.io/badge/Web%20App-Zero%20Dependencies-orange.svg)](index.html)
[![Course: CSET302](https://img.shields.io/badge/CSET302-Automata%20Theory%20%26%20Computability-indigo.svg)](index.html)

**Course:** CSET302 - Automata Theory and Computability  
**Topic:** #14 &mdash; *Mealy &harr; Moore Conversion*  
**Team Size:** 5 Members  
**Milestones Covered:** Milestone 1 (5 Marks) & Milestone 2 (9 Marks) &mdash; **Total 14 Marks**

---

## 🎯 Project Overview & Expected Functionality
As specified in **Topic 14 of the CSET302 Simulator Design Pool**:
> *"Convert between machines while preserving and displaying output behaviour."*

This simulator implements bidirectional conversion between Mealy machines (output on transitions) and Moore machines (output on states) while strictly verifying and demonstrating the formal **Output Equivalence Theorem**:
$$\lambda_{Moore}(w) = \lambda_{Moore}(q_0) \cdot \lambda_{Mealy}(w)$$

---

## 🚀 Quick Start Guide

### Option 1: Standalone Browser (Zero Installation)
Simply double click or open **`index.html`** in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, Safari).
No web server, node, or npm dependencies required!

### Option 2: Run Local Python Server & REST API
```bash
python local_server.py
```
Then visit **`http://localhost:8000`** in your browser.

### Option 3: Run Automated Verification Tests (Pytest)
```bash
pip install -r requirements.txt
python -m pytest python_core/test_converter.py -v
```

### Option 4: Generate Academic Report PDF
```bash
python generate_report_pdf.py
```
Produces `CSET302_Topic14_Mealy_Moore_Simulator_Report.pdf` formatted to the exact evaluation rubrics.

---

## 🏗️ Minimum Technical Standard Adherence

The simulator strictly satisfies the mandatory pipeline:
$$\text{User Input} \longrightarrow \text{Algorithm} \longrightarrow \text{Step-by-Step Processing / Visualization} \longrightarrow \text{Result} \longrightarrow \text{Validation}$$

1. **Dynamic Input:**
   - Visual transition matrix grid editor with real-time state, symbol, and transition additions.
   - Pre-loaded library with 6 classic automata:
     - *Sequence Detector '101'* (Overlapping patterns)
     - *2's Complement Generator* (LSB to MSB stream)
     - *1's Complement Bit Inverter* (Single-state edge case)
     - *Even/Odd Parity Bit Generator* (Moore machine)
     - *Binary Modulo-3 Counter* (Multi-symbol output $\Delta = \{0, 1, 2\}$)
     - *Multi-Split State Challenge* (State entered with 3 distinct outputs)
   - Full JSON import & export.

2. **Correct Algorithm:**
   - **Mealy to Moore Conversion:** Incoming transitions analyzer, state-splitting into $(q, b)$, initial state handling, and automated BFS reachability pruning.
   - **Moore to Mealy Conversion:** Output inheritance on incoming transitions: $\lambda_{Mealy}(q, a) = \lambda_{Moore}(\delta(q, a))$.

3. **Step-by-Step Processing:**
   - Dedicated interactive walkthrough stepper with:
     - Incoming output analysis table ($Out(q)$)
     - State splitting table ($q \to q_b$)
     - Transition function construction table
     - BFS Reachability analysis & state minimization log

4. **Visualization:**
   - Side-by-side interactive SVG state diagrams:
     - Mealy states with transition labels `input / output`
     - Moore states with node labels `state / output`
     - Clean curved transitions for bidirectional arcs and self-loops
     - Draggable vertices with physics relaxation
     - Pan & zoom controls with SVG vector export

5. **Result & Validation:**
   - Single-string live simulation with play, pause, step-forward, step-back, and speed controls.
   - Synchronized moving tape cursors for Input String, Mealy Output, and Moore Output.
   - Automated Equivalence Assertion highlighting the 1-symbol prefix property:
     $$\text{Moore Output} = \lambda(q_0) + \text{Mealy Output}$$
   - Batch Test Runner evaluating multiple strings with Pass/Fail status and execution times.

---

## 👥 5-Member Team Contribution & Viva Voce Guide

| Team Member | Role | Key Contributions | Viva Assessment Focus |
|-------------|------|-------------------|-----------------------|
| **Member 1** | Formal Modeling & Architecture Lead | 6-tuple formal data models (`automata_models.py`), input validation, JSON schema, Milestone-1 specifications. | Formal 6-tuple definitions, domain and codomain of $\delta$ and $\lambda$. |
| **Member 2** | Mealy &rarr; Moore Conversion Lead | State-splitting algorithm, incoming transition analysis, initial state resolution, and step-by-step conversion audit generator. | State splitting logic, maximum state bound $\|Q_{Moore}\| \le \|Q_{Mealy}\| \times \|\Delta\|$, start state output. |
| **Member 3** | Moore &rarr; Mealy & Equivalence Proofs | 1-step target-output inheritance, formal mathematical induction proof, proof of string lengths ($n$ vs $n+1$). | Why Moore $\to$ Mealy preserves state count; equivalence theorem proof. |
| **Member 4** | Interactive Graph Visualizer & Animation | SVG transition diagram visualizer with draggable nodes, curved arcs, self-loops, and real-time step animations. | Visual distinctions of Mealy vs Moore, layout coordinates, SVG path math. |
| **Member 5** | Verification Suite & Testing Lead | Automated batch test suite, preset library, BFS reachability pruning, Pytest unit tests. | Edge cases (unreachable states, empty string $\epsilon$, single-state), Pytest coverage. |

---

## 📁 Repository Structure

```
Automata_simulator/
├── .github/
│   └── workflows/
│       └── test.yml             # GitHub Actions CI workflow (automated tests on push)
├── .gitignore                   # Clean ignore rules (caches, secrets, OS junk)
├── LICENSE                      # MIT Open Source License
├── requirements.txt             # Python dependencies (pytest, reportlab)
├── index.html                   # Main interactive web simulator (Zero setup)
├── css/
│   └── styles.css               # Modern dark-themed styling, animations, responsive grid
├── js/
│   ├── mealy_moore_core.js      # Formal Mealy & Moore classes and bidirectional conversion
│   ├── presets.js               # 6 Pre-configured classic and edge-case automata
│   ├── graph_visualizer.js      # Interactive SVG state diagram renderer (drag/zoom/pan)
│   ├── simulation_engine.js     # Synchronized string simulation with tape animation
│   └── app.js                   # Application coordinator and UI event bindings
├── python_core/
│   ├── automata_models.py       # Formal 6-tuple classes in Python
│   ├── converter.py             # Conversion algorithms with audit trail in Python
│   └── test_converter.py        # Pytest test suite with 100% test pass rate
├── local_server.py                    # Lightweight Python HTTP server & REST API
├── generate_report_pdf.py       # Publication-ready PDF report generator using ReportLab
├── CSET302_Topic14_Mealy_Moore_Simulator_Report.pdf  # Generated 3-page academic report
└── README.md                    # Project documentation
```

---

## 📤 Uploading to GitHub

To push this repository to GitHub, run the following commands in your terminal:

```bash
# 1. Initialize git repository
git init

# 2. Stage all project files (safe files only, caches are ignored via .gitignore)
git add .

# 3. Create the initial commit
git commit -m "feat: complete CSET302 Topic 14 Mealy <-> Moore Automata Simulator"

# 4. Set branch to main
git branch -M main

# 5. Add your GitHub remote repository (replace with your repo URL)
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY_NAME>.git

# 6. Push to GitHub
git push -u origin main
```
