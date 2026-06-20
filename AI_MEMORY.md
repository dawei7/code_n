# AI Project Memory: cOde(n)

**Created by:** Antigravity (Gemini)
**Date:** 2026-06-18
**Purpose:** Provide context, architectural details, and workflows for future AI agents (Claude, Kilocode, Gemini, etc.) working on this repository.

## 1. Project Overview
**Name:** cOde(n)
**Description:** A learning game for Python algorithms and data structures, inspired by *The Farmer Was Replaced*. It tracks reads, writes, compares, and swaps of data structures to ensure solutions fit within the required complexity class.
**Previous AI Agents:** Kilocode (used `.kilo/` directory for worktrees/sessions), Claude. 

## 2. Architecture & Tech Stack
- **Frontend (`web/`):** React, Vite, TypeScript, Tailwind, Monaco Editor, Zustand.
- **Backend (`server/`):** FastAPI, Uvicorn, Python. Acts as a wrapper over the core engine.
- **Desktop Wrapper (`electron/`):** Electron. Bundles the React app and PyInstaller-bundled FastAPI server into a portable Windows `.exe`.
- **Core Engine (`code_n/`, `challenges/`, `optimal_solutions/`):** Pure Python engine evaluating algorithm constraints and performance.

## 3. Key Directories
- `web/`: Contains the frontend UI and visualizers.
- `server/`: Contains FastAPI routing (`/api/*`).
- `electron/`: Contains Electron wrapper script and handles building `cOde(n).exe`.
- `challenges/`: Contains all problem definitions (e.g. `challenges/algorithms/<category>.py`).
- `docs/`: Reference documentation for algorithms, built dynamically in the app's Reference tab.

## 4. Developer Workflows

### Running Locally (Dev Mode)
**Terminal 1 (Backend):**
```bash
cd c:/dawei7/code_n
.venv/Scripts/python.exe -m uvicorn server.app.main:app --port 8000 --reload
```

**Terminal 2 (Frontend):**
```bash
cd c:/dawei7/code_n/web
npm install # first time
npm run dev
```
UI available at `http://localhost:5173`.

### Running Electron Wrapper Locally
```bash
cd c:/dawei7/code_n/electron
npm start
```
*Note: Set `CODEN_DEVTOOLS=1` to open Chrome DevTools in Electron.*

### Testing
```bash
# Engine tests (critical path)
.venv/Scripts/python.exe -m unittest discover -s tests

# Server tests
.venv/Scripts/python.exe -m unittest discover -s server/tests -t .

# Web tests
cd web && npx tsc --noEmit
```

### Production Build
Builds the complete Windows `.exe`:
```bash
.venv/Scripts/python.exe build_app.py
```

## 5. Standard Tasks
- **Adding a Challenge:** Edit or create `challenges/algorithms/<category>.py`. Add `AlgorithmSpec(...)` with ID, complexity, sample inputs, and reference solution. The server and UI will automatically reflect this.
- **Writing Algorithm Docs:** Copy `docs/_template.md` to `docs/algorithms/<category>/<id>_<slug>.md`.

## 6. AI Guidelines for this repo
- Always ensure `tests` (engine tests) stay green; there are currently 102 tests (83 engine + 19 server).
- For UI changes, remember the app uses Tailwind and standard React hooks/Zustand. Avoid breaking the Monaco editor integration.
- Desktop releases are packaged as directory (`dir` target) to avoid NSIS installer overhead. The `coden-server.exe` runs in GUI subsystem mode (`console=False`) to allow Electron to parse stdout port bindings.
