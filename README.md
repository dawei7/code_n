# cOde(n) — The Interactive Algorithms Arena

**cOde(n)** is a premium, gamified learning platform and results visualizer for Python algorithms and data structures. Inspired by programming automation games, it provides developers and computer science students with a structured arena to write, debug, and optimize classic computer science challenges.

Rather than relying on inaccurate runtime execution timers, **cOde(n)** analyzes solutions using static AST (Abstract Syntax Tree) operation counting. Your solutions are validated not only for functional correctness but also for structural complexity, ensuring they strictly adhere to their theoretical asymptotic bounds.

---

## 🚀 Key Features

* **Direct VSCode Integration**: The actual coding and debugging happen in your local VSCode workspace. Set breakpoints, inspect local variables, and run tests via standard VSCode debug tools (`F5`), while cOde(n) serves as your primary visual cockpit.
* **AST Complexity Budgeting**: Solutions are analyzed statically based on operation counts nested within loop structures. Verdicts verify that the algorithm stays within the mathematical complexity budget (e.g., $O(n \log n)$) for the input size $n$.
* **University-Level LaTeX Reference Sheets**: Includes comprehensive, mathematically rigorous formal specifications for every algorithm. The references detail state-space definitions, loop invariants, algebraic recurrence relations, and complexity proofs in formatted LaTeX.
* **Rich Aesthetic UI**: A modern, dark-mode dashboard featuring glassmorphic components, fluid animations, and real-time visualization of complexity bands.
* **Locally Hosted & Self-Updating**: Built as a packaged Electron application running a local FastAPI server, featuring fully automated updates via GitHub Releases.

---

## 🛠️ How it Works

```
                     VSCODE WORKSPACE                    cOde(n) DESKTOP
                 ┌──────────────────────┐            ┌────────────────────┐
                 │  solutions/sort_01.py│            │                    │
                 │                      │            │  Visual Verdict    │
   1. Open ────▶ │  def solve(data):    │ ────▶      │  [CORRECT]         │
                 │      # Edit here     │      │     │  AST Ops: 180      │
                 │                      │      │     │  Budget: 250       │
   2. F5  ──────▶│  python run_solution │ ────┼────▶│  asymptotic band:  │
                 │  (evaluates AST code)│            │  O(n log n)        │
                 └──────────────────────┘            └────────────────────┘
```

1. **Select a Challenge**: Pick one of the 264 curated challenges from the sidebar navigator inside the cOde(n) app.
2. **Open in VSCode**: Click the "Open in VSCode" button to auto-scaffold a clean starter file at `solutions/<id>.py` containing the precise function signature and sample input documentation.
3. **Write and Debug**: Write your implementation in VSCode. Run the solution using the custom task runners or debug step-by-step.
4. **View Verdicts**: The code is evaluated via the `code_n` engine. The complexity and correctness results are immediately mapped and displayed in cOde(n).

---

## 📂 Project Architecture

The codebase is split into a robust client-server architecture packaged for desktop use:
* **Frontend (`web/`)**: React, Vite, TypeScript, TailwindCSS, Zustand. A fast, premium web interface displaying challenge parameters, complexity curves, and mathematical references.
* **Backend (`server/`)**: FastAPI, Uvicorn, Python. Serves the API, reads file updates, runs the AST analyzer, and exposes the challenge registry.
* **Core Engine (`code_n/` & `challenges/`)**: The mathematical heart of cOde(n). Defines problem specs, validation inputs, verification functions, and bounds classifiers.
* **Desktop Wrapper (`electron/`)**: Electron wrapper that bundles the React static bundle and the PyInstaller-compiled FastAPI server into a single portable `.exe` with auto-update mechanisms.

---

## 💻 Developer Guide

### Prerequisites
* Python 3.12+ (dependencies managed in virtual environment)
* Node.js 18+ (for building Electron and React assets)

### Local Development Flow
To run the full development environment, open two terminals:

**Terminal 1 (FastAPI Server)**:
```powershell
# Set up environment variables and launch FastAPI reload server
.venv\Scripts\python.exe -m uvicorn server.app.main:app --port 8000 --reload
```

**Terminal 2 (React Frontend)**:
```bash
cd web
npm install
npm run dev
```
Open `http://localhost:5173` to interact with the application.

### Running the Electron App locally
To start the desktop shell pointing to your local assets:
```bash
cd electron
npm install
npm start
```
*Tip: Set the environment variable `CODEN_DEVTOOLS=1` to launch Chrome Developer Tools alongside the desktop window.*

### Testing Suite
Always run the validation suite to verify core logic:
```powershell
# Run the core engine tests (108 tests)
.venv\Scripts\python.exe -m pytest tests/ server/tests/
```

---

## 🚀 Release Pipeline

To release a new version of the app with automatic updates:
1. Ensure your working tree is clean on the `main` branch.
2. Set the `GH_TOKEN` environment variable in your shell.
3. Run the automated release orchestrator:
```powershell
# Bumps version, runs builds (Vite + PyInstaller + Electron), tags git, and pushes to GitHub
.venv\Scripts\python.exe release.py --patch --cleanup-old
```

---

## 📝 License
This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
