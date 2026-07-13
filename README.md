# cOde(n) - The Interactive Algorithms Arena

**cOde(n)** is a desktop learning environment for practicing Python algorithms and data structures. It brings together an in-app Monaco editor, Python debugging, challenge reference material, progress tracking, and complexity feedback in one focused workspace.

cOde(n) judges correctness separately from complexity. Authored benchmark tiers
compare how the user/reference runtime ratio changes as the workload grows,
using paired measurements designed to reduce ordinary timing noise.

---

## Key Features

* **In-app coding and debugging**: Write solutions in the cOde(n) editor, set breakpoints, inspect locals, and step through Python without leaving the app.
* **Complexity scaling**: Multi-size benchmarks compare the growth of a solution against the package's optimal same-language reference while tolerating reasonable constant-factor implementation differences.
* **Reference and analysis tabs**: Challenge documentation, formal notes, examples, source links, and runtime analysis stay next to the coding surface.
* **Progress tracking**: Completion records, solution versions, profiles, and career-mode unlocks are persisted locally.
* **LeetCode practice views**: Browse the canonical problem library through official study plans, company tags, NeetCode subsets, or the AlgoMaster 600, 300, 150, and 75 lists without duplicating challenge data.
* **Local desktop packaging**: Electron hosts the React frontend and launches a local FastAPI server for the Python engine.

---

## How It Works

1. **Select a challenge** from the sidebar.
2. **Edit the solution** in the cOde(n) tab. The app keeps three explicit versions in the writable user profile, for example `dsa/leetcode/1_two-sum/user_solutions/python_v1.py`. Bundled challenge data stays read-only.
3. **Run or debug** the solution. Practice mode uses your chosen `n` and seed; real-test mode lets the server pick fresh inputs.
4. **Review the verdict** in the result and complexity tabs, including correctness, per-tier runtime ratios, scaling behavior, and return values.
5. **Use references** when you want the official problem link, explanation, mathematical notes, or a stronger solution strategy.

---

## Project Architecture

The codebase is split into a client-server desktop app:

* **Frontend (`web/`)**: React, Vite, TypeScript, TailwindCSS, Zustand, Monaco, markdown rendering, and the in-app debugger UI.
* **Backend (`server/`)**: FastAPI routes, debugpy/DAP bridge, challenge registry access, progress persistence, solution storage, and run orchestration.
* **Core engine (`engine/` and `challenges/`)**: Challenge specs, input generation, verification functions, runtime measurement, and complexity classification.
* **Desktop wrapper (`electron/`)**: Electron shell, packaged server launch, app updates, and desktop resource staging.

---

## Developer Guide

### Prerequisites

* Python 3.12+
* Node.js 18+
* Project dependencies installed in `.venv`, `web/node_modules`, and `electron/node_modules`

### Local Development

For the normal desktop workflow, use the fast development launcher:

```powershell
npm.cmd run dev
```

It starts Vite and Electron together, assigns free local ports, and lets Vite
serve the UI directly with hot reload. It does not run a production web build
before opening the app.

For a browser-only workflow, run the backend and frontend separately.

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

### Documentation Sources

- [`AGENTS.md`](AGENTS.md): authoritative architecture, invariants, storage
  rules, and verification workflow for coding agents and maintainers.
- [`BENCHMARKING.md`](BENCHMARKING.md): Two Sum exemplar, benchmark-tier
  contract, complexity verdict semantics, and corpus migration checklist.
- [`LEETCODE_SUBMISSIONS.md`](LEETCODE_SUBMISSIONS.md): secure account
  connection, platform-native verified artifacts, one-click submission, and
  the long-term per-problem verification workflow.
- `dsa/leetcode/<frontend_id>_<slug>/doc.md`: canonical per-problem reference.
- [`RELEASING.md`](RELEASING.md): Windows packaging, signing, publishing, and
  updater procedures.

There is intentionally no parallel `docs/` tree. The app serves this README as
its overview and reads challenge documentation directly from each LeetCode
package.

### Difficulty metadata

The app always preserves LeetCode's official `Easy`, `Medium`, or `Hard` tier.
Where available, it adds the contest Elo calculated by the
[ZeroTrac LeetCode Problem Rating project](https://zerotrac.github.io/leetcode_problem_rating/#/).
ZeroTrac does not cover every problem, including problems from Weekly Contests
1–62. Only for those legacy contest problems, the app retains the former
acceptance-percentile sublevel and labels it explicitly as
`Legacy estimate n/10`; it is never presented as an Elo. Other unrated or
non-contest problems show only LeetCode's official tier.

Refresh the bundled sparse rating map with:

```powershell
.\.venv\Scripts\python.exe tools\sync_zerotrac_ratings.py
```

The pinned upstream revision and update timestamp are stored in
`dsa/leetcode/_meta/zerotrac-ratings.json`. ZeroTrac's required MIT notice is
bundled beside it as `zerotrac-LICENSE.txt`. The same metadata file records the
fixed Weekly Contest 1–62 membership and the revision used to verify it.

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
