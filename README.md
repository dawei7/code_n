# cOde(n) - The Interactive Algorithms Arena

**cOde(n)** is a desktop learning environment for practicing Python algorithms and data structures. It brings together an in-app Monaco editor, Python debugging, challenge reference material, progress tracking, and complexity feedback in one focused workspace.

Instead of relying on noisy runtime timers, cOde(n) analyzes solutions with static AST operation counting. Runs are judged for correctness and for whether the implementation matches the expected asymptotic complexity.

---

## Key Features

* **In-app coding and debugging**: Write solutions in the cOde(n) editor, set breakpoints, inspect locals, and step through Python without leaving the app.
* **AST complexity budgeting**: Solutions are analyzed by counting operations inside the source structure, including loops and calls, so verdicts can compare your work against the expected complexity class.
* **Reference and math tabs**: Challenge documentation, formal notes, examples, and source links stay next to the coding surface.
* **Progress tracking**: Completion records, best operation counts, profiles, and career-mode unlocks are persisted locally.
* **Local desktop packaging**: Electron hosts the React frontend and launches a local FastAPI server for the Python engine.

---

## How It Works

1. **Select a challenge** from the sidebar.
2. **Edit the solution** in the cOde(n) tab. The app persists the source to `solutions/<id>.py`.
3. **Run or debug** the solution. Practice mode uses your chosen `n` and seed; real-test mode lets the server pick fresh inputs.
4. **Review the verdict** in the result and complexity tabs, including correctness, operation counts, complexity class, and return values.
5. **Use references** when you want the official problem link, explanation, mathematical notes, or a stronger solution strategy.

---

## Project Architecture

The codebase is split into a client-server desktop app:

* **Frontend (`web/`)**: React, Vite, TypeScript, TailwindCSS, Zustand, Monaco, markdown rendering, and the in-app debugger UI.
* **Backend (`server/`)**: FastAPI routes, debugpy/DAP bridge, challenge registry access, progress persistence, solution storage, and run orchestration.
* **Core engine (`code_n/` and `challenges/`)**: Challenge specs, input generation, verification functions, AST operation counting, and complexity classification.
* **Desktop wrapper (`electron/`)**: Electron shell, packaged server launch, app updates, and desktop resource staging.

---

## Developer Guide

### Prerequisites

* Python 3.12+
* Node.js 18+
* Project dependencies installed in `.venv`, `web/node_modules`, and `electron/node_modules`

### Local Development

Run the backend:

```powershell
.\.venv\Scripts\python.exe -m uvicorn server.app.main:app --port 8000 --reload
```

Run the frontend:

```powershell
cd web
npm.cmd install
npm.cmd run dev
```

Open `http://localhost:5173`.

### Desktop Shell

```powershell
cd electron
npm.cmd install
npm.cmd start
```

Set `CODEN_DEVTOOLS=1` to open Chromium DevTools with the desktop window.

### Validation

```powershell
.\.venv\Scripts\python.exe -m pytest tests server/tests
npm.cmd run typecheck --prefix web
npm.cmd run build --prefix electron
```

---

## Release Pipeline

1. Ensure the intended branch and working tree state are ready.
2. Set `GH_TOKEN` in the shell.
3. Run:

```powershell
.\.venv\Scripts\python.exe release.py --patch --cleanup-old
```

---

## License

This project is licensed under the [MIT License](LICENSE).
