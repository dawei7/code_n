# cOde(n)

A learning game for Python algorithms and data structures, inspired by
*The Farmer Was Replaced*. The player writes a `solve(...)` function
and the engine wraps the inputs in *tracked* data structures that
count every read, write, compare, and swap. A solution passes only
when it is both correct and stays within the operation budget implied
by the required complexity class.

**Similar to "The Farmer Was Replaced" — but for algorithms, entirely in Python.**

## Architecture (2026-06-07 rebuild)

The cOde(n) frontend moved off Pygame in 2026-06-07. The Python
engine is preserved as-is; the renderer and packaging were replaced
with a server-client stack:

```
React + Tailwind (Monaco editor + DOM-based visualizer)
   |
   | fetch /api/*
   v
FastAPI (uvicorn on 127.0.0.1:<port>)
   |
   | uses
   v
code_n engine + challenges registry   ← UNTOUCHED
```

- **Backend:** FastAPI in `server/` (wraps the engine)
- **Frontend:** React + Vite + TypeScript + Tailwind + Monaco + Zustand in `web/`
- **Desktop wrapper:** Electron in `electron/` (dev launcher only; full .exe build is a follow-up)
- **Engine:** `code_n/`, `challenges/`, `optimal_solutions/`, the 207-test engine suite — **untouched**

See `legacy/README.md` for the old Pygame/CLI build (still functional, archived).

## How to run the dev workflow

You need two terminals. The Vite dev server (port 5173) proxies
`/api/*` to the FastAPI server (port 8000).

**Terminal 1 — FastAPI server:**
```bash
cd "c:/dawei7/code_n"
.venv/Scripts/python.exe -m uvicorn server.app.main:app --port 8000
```

**Terminal 2 — Vite dev server:**
```bash
cd "c:/dawei7/code_n/web"
npm install  # first time only
npm run dev
```

Open `http://localhost:5173`. Click `sort_01` in the left rail, then
"Show solution" → "Run" to see the algorithm step through.

### Hot reload

- FastAPI: add `--reload` to the uvicorn command
- Vite: hot-reload is on by default in dev

## How to run the Electron desktop wrapper

The Electron dev launcher spawns the FastAPI server as a child
process, waits for it to become healthy on `/api/health`, then opens
a `BrowserWindow` at the server's URL. The FastAPI server mounts
`web/dist/` as static files, so the React app loads from the same
process that serves the API.

```bash
# 1. Build the React app (one time, or after React changes)
cd "c:/dawei7/code_n/web"
npm run build

# 2. Start Electron (it builds its main process + spawns uvicorn)
cd "c:/dawei7/code_n/electron"
npm install  # first time only
npm start
```

A native window opens at the FastAPI server's URL (a random free
port — the launcher parses it from uvicorn's stdout). On window
close, the launcher kills the uvicorn process so it doesn't
outlive the app.

**Set `CODEN_DEVTOOLS=1`** to open Chrome DevTools in the
BrowserWindow for debugging.

### Production build (desktop .exe)

The `build_app.py` orchestrator runs the full pipeline: build the
React app, bundle the FastAPI server with PyInstaller, compile the
Electron main process, and package a desktop app via
electron-builder.

```bash
cd "c:/dawei7/code_n"
.venv/Scripts/python.exe build_app.py
```

The output is `electron/release/win-unpacked/cOde(n).exe`
(~170 MB) — double-click it to launch. The folder also contains
`resources/coden-server/coden-server.exe` (the bundled Python
server, ~8 MB). No Python, no Node, no venv required on the target
machine.

**Why the `dir` target, not `portable`:** electron-builder's
`portable` target uses NSIS and can hang on first build while it
downloads + runs `makensis.exe`. The `dir` target is the raw
unpacked Electron app — same user experience (double-click the
.exe), no NSIS step.

**PyInstaller stdout gotcha:** the bundled `coden-server.exe` is
built with `console=False` in [server.spec](server/server.spec).
PyInstaller's bootloader captures stdout to its own console window
when `console=True`, which breaks the pipe Electron uses to read
the server's port. `console=False` makes the .exe a GUI subsystem
app that inherits stdio from the parent, so Electron can read the
"Uvicorn running on..." line normally.

The bundle contains:
- The Electron 31.7.7 runtime + Chromium
- The compiled Electron main process (TypeScript → JS)
- The PyInstaller-bundled `coden-server.exe` (Python 3.13 + FastAPI
  + uvicorn + the engine + all 25 challenges)
- The compiled React app (`web/dist/`)
- The coden icon

When the .exe runs, the Electron main process detects the bundled
server at `process.resourcesPath/coden-server/coden-server.exe`,
spawns it, polls `/api/health`, then opens a BrowserWindow at
the server's URL. The server picks a free port (default: 0) and
prints it on stdout; the launcher parses the port and loads the
UI.

`progress.json` + `solutions/` live in the user's writable app
data dir (`%APPDATA%/cOde(n)` on Windows, set by
`app.getPath('userData')` in the launcher).

## How to run the tests

```bash
cd "c:/dawei7/code_n"

# Engine tests (the load-bearing 207 — must always be green)
.venv/Scripts/python.exe -m unittest discover -s tests

# Server tests (19 — covers all API endpoints + the end-to-end run)
.venv/Scripts/python.exe -m unittest discover -s server/tests -t .

# Web typecheck
cd web && npx tsc --noEmit

# Web production build
cd web && npx vite build
```

## How to add a new challenge

The engine's spec framework makes this a single-file change.

1. Open the relevant `challenges/algorithms/<category>.py` (or create a new one).
2. Add a `Sample(...)` if you want the explore view to show input/output.
3. Add an `AlgorithmSpec(...)` to the `SPECS` list with: `id`, `name`,
   `category`, `difficulty`, `required_complexity`, `description`,
   `source_url`, `params`, `inputs`, `returns`, `source` (the canonical
   optimal solution as Python), `setup_fn`, `verify_fn`, plus optional
   `samples`, `expected_operations`, `max_n`, `parents`, `children`.

The server's `GET /api/challenges` list and the React challenge rail
pick the new spec up automatically on the next page load.

## How to add a new visualizer (post-MVP)

The MVP only has a 1D sort visualizer (in
`web/src/components/Visualizer.tsx`). Adding a 2D grid visualizer
(BFS/DFS) follows the same shape: derive `data: number[][]` and
`cellStates: CellState[][]` from the current trace frame's locals,
then render with CSS Grid. The `useStepPlayer` hook and the
`useAppStore` slice are challenge-agnostic.

## Legacy build

The old Pygame/CLI build is preserved in `legacy/`. It still
works:

```bash
cd "c:/dawei7/code_n"
.venv/Scripts/python.exe main.py                                          # CLI menu
.venv/Scripts/python.exe run_challenge.py --pygame intro_01 --n 8 --seed 1
.venv/Scripts/python.exe build_windows_exe.py                             # rebuild old exe
```

The Pygame exe is at `dist/cOde(n)/cOde(n).exe` (gitignored).
See `legacy/README.md` for the full archive notes.

## License

TBD
