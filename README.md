# cOde(n)

**A free, offline-first learning environment for LeetCode-indexed algorithm
problems.**

cOde(n) exists to give every student and working professional a practical way
to study algorithms, prepare for interviews, and improve implementation skills
without placing essential explanations behind another learning platform.

For each completed problem, the goal is to provide:

- the exact LeetCode frontend ID, title, difficulty, and official problem link;
- an independently written, concise explanation of the problem and its
  important boundary conditions;
- correctness cases and three complexity-sensitive benchmark tiers;
- an optimal app-local reference implementation;
- a platform-native submission artifact; and
- remote verification that the exact artifact was **Accepted by LeetCode's
  judge**.

“Accepted” describes a recorded judge result. It does not mean that LeetCode
approved, sponsored, or endorsed cOde(n).

> cOde(n) is an independent open-source project created and maintained by
> **David Schmid**. It is not affiliated with, sponsored by, or endorsed by
> LeetCode LLC.

## What learners get

- **One focused desktop workspace:** read, code, run, debug, and review results
  without switching to an external IDE.
- **Original explanations:** every migrated package restates the task in
  independent language and teaches the reasoning behind the selected method.
- **Guided representative examples:** package-authored Markdown lessons work
  through carefully selected inputs with tables, diagrams, mathematical
  notation, correctness reasoning, and explicit traps. They teach how and why
  the method works without revealing solution code.
- **Publication-quality study PDFs:** PDF controls beside the left-pane download
  controls export one problem, a hierarchy level, or all currently shown
  problems through native Save As. Bundles follow set order and place each
  problem's Reference before its Guided Example in a professional light-mode
  A4 layout. A linked hierarchical contents page records the UTC generation
  time, and every later page links back to it. The PDF menu can omit solutions
  or append each problem's primary-language solution (Python 3 for ordinary
  algorithms; source-native SQL, Bash, JavaScript, or another declared default
  where required).
- **Verified solutions:** a native submission is marked verified only after the
  exact stored source receives an Accepted result from LeetCode.
- **Correctness and complexity as separate skills:** ordinary cases check the
  answer, while authored benchmark tiers test whether runtime growth matches
  the required complexity class.
- **Useful learning paths:** browse the same canonical packages through
  LeetCode categories and study plans, company and topic views, NeetCode views,
  or AlgoMaster collections. These are views, never duplicate problem roots.
- **Local progress and solutions:** profiles, progress, and three personal
  solution versions per language stay in the writable local user-data
  directory. Bundled learning resources remain read-only.

## Project status

Version `0.1.0` is an active corpus migration, not a claim that every package is
finished. The repository indexes 3,985 canonical frontend IDs. At this version,
819 packages are locally complete and remotely verified, and documentation has
been authored through frontend ID 822. The generated migration reports in
[`dsa/leetcode/_reports/`](dsa/leetcode/_reports/) are the current source of
truth.

The long-term objective is one complete educational package for every indexed
problem through frontend ID 3985.

## How a problem package is organized

Each problem has one canonical home:

```text
dsa/leetcode/<frontend_id:04d>_<slug>/
  metadata.json
  doc.md
  cases.json
  benchmark.json
  guided_example.md                 # optional code-free worked example
  solution_variants.json           # Optimal-first branch manifest
  variants/
    optimal/
      approach.md
      submission.json              # present after remote verification
      solutions/
        python.py                   # app-local solve(...) implementation
        leetcode_python3.py         # native candidate when available
    simplified/                     # optional, only after reviewed verification
      approach.md
      submission.json
      solutions/
```

The directory prefix is the four-digit, zero-padded frontend ID, so `lc_1`
lives in `0001_two-sum` and repository listings remain in numeric order. The
padding is a path-formatting detail; metadata and challenge IDs remain `1` and
`lc_1`.

The shared package document contains the goal, function contract, and examples.
Each branch owns its Required Complexity, educational approach, implementations,
and submission evidence under `variants/`, so the shared problem contract stays
separate from algorithm-specific material.

## Copyright, attribution, and LeetCode

This repository is **not a mirror of LeetCode**. Its copyright rule is simple:
preserve the meaning of an algorithmic task, but do not copy LeetCode's
protected expression.

### What cOde(n) publishes

- factual identifiers needed to identify a problem, such as its frontend ID,
  title, slug, difficulty, topics, and official URL;
- original problem narratives, explanations, mathematical reasoning, cases,
  and benchmarks written for cOde(n);
- independently written source code implementing the underlying algorithms;
  and
- third-party material only when its license permits redistribution, with the
  required notice kept beside it.

### What cOde(n) does not claim

- It does not claim ownership of LeetCode's website, branding, problem
  statements, editorials, illustrations, or proprietary solution text.
- It does not treat attribution, a hyperlink, or an educational purpose as
  permission to reproduce protected material.
- It does not intentionally publish verbatim full LeetCode statements or
  editorials. The official link is provided for readers who want the source
  presentation.
- It does not bypass LeetCode account or Premium controls for official pages or
  submissions.

### Why the project uses independent explanations and implementations

Copyright protects an author's particular expression. It does not protect the
underlying idea, procedure, method of operation, system, process, or
mathematical concept as such. This idea-expression distinction is explained by
the [World Intellectual Property Organization](https://www.wipo.int/en/web/copyright/protection)
and the [U.S. Copyright Office](https://www.copyright.gov/what-is-copyright/).

That distinction does **not** make LeetCode's prose or source code free to copy.
Those are concrete expressions and may be protected. cOde(n) therefore teaches
the same algorithmic concepts through newly written prose and independently
implemented code instead of reproducing LeetCode's wording, editorials, or
solutions.

LeetCode's current [Terms of Service](https://leetcode.com/terms/) describe its
questions, solutions, and related platform material as protected content and
also impose restrictions separate from copyright, including restrictions on
automated access. Anyone using optional synchronization or submission tools is
responsible for complying with those current Terms and applicable law.

This section documents the project's copyright-respect policy; it is not a
legal opinion or a guarantee about every jurisdiction. If a rights holder
identifies material that should be removed, relicensed, or rewritten, please
open an issue with the exact file and basis for the request so it can be
reviewed promptly.

## Product architecture

- **`web/`:** React, TypeScript, Vite, Zustand, Monaco, reference and guided
  example rendering, career views, and the in-app debugger interface.
- **`server/`:** FastAPI routes, execution harnesses, validation, benchmark
  analysis, DAP integration, progress storage, and user-solution storage.
- **`engine/` and `challenges/`:** language contracts, challenge types,
  complexity logic, tracing, starter generation, and the canonical registry.
- **`electron/`:** Windows desktop shell, local server lifecycle, secure
  credential storage, updates, and packaging.
- **`dsa/leetcode/`:** the canonical problem packages and generated migration
  reports.

## Local development

### Prerequisites

- Python 3.12 or newer
- Node.js 18 or newer
- dependencies installed in `.venv`, `web/node_modules`, and
  `electron/node_modules`

Start the normal desktop development workflow:

```powershell
npm.cmd run dev
```

This launches Vite and Electron together with hot reload. It does not put a
production web build on the interactive startup path.

For a browser-only workflow, run the backend and frontend separately:

```powershell
.\.venv\Scripts\python.exe -m uvicorn server.app.main:app --port 8000 --reload
npm.cmd run dev --prefix web
```

Then open `http://localhost:5173`.

## Validation

Run the complete repository checks with:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
npm.cmd run build --prefix web
npm.cmd run build --prefix electron
```

For canonical dataset documentation work, also run:

```powershell
.\.venv\Scripts\python.exe tools\check_leetcode_dataset.py
.\.venv\Scripts\python.exe -m pytest server\tests\test_dynamic_docs.py -q
```

## Maintainer documentation

- [`AGENTS.md`](AGENTS.md): authoritative architecture, invariants, storage
  boundaries, documentation style, and verification workflow.
- [`BENCHMARKING.md`](BENCHMARKING.md): benchmark-tier and complexity-verdict
  specification.
- [`LEETCODE_SUBMISSIONS.md`](LEETCODE_SUBMISSIONS.md): native candidate,
  remote verification, and submission-manifest rules.
- [`RELEASING.md`](RELEASING.md): Windows packaging, signing, publishing, and
  updater procedures.
- [`dsa/leetcode/_template.md`](dsa/leetcode/_template.md): canonical
  per-problem documentation contract.

## License

The original cOde(n) source code and documentation are released under the
[MIT License](LICENSE), copyright © 2026 David Schmid. That license applies only
to material David Schmid has the right to license; it does not relicense
LeetCode's website or any separately identified third-party work.

LeetCode is a trademark of LeetCode LLC. All third-party names and marks remain
the property of their respective owners and are used only to identify the
corresponding source or compatibility target.
