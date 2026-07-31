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
- **English-only learning surface:** the interface, references, guided examples,
  reports, and supporting documentation use one maintained natural language.
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
  LeetCode categories, study plans, Quests, company and topic views, NeetCode
  views, or AlgoMaster collections. These are views, never duplicate problem
  roots.
- **Local progress and solutions:** profiles, progress, and three personal
  solution versions per language stay in the writable local user-data
  directory. Bundled learning resources remain read-only.

## Project status

Version `0.2.2` is an active corpus migration, not a claim that every package is
finished. The repository indexes its final corpus of 4,005 canonical frontend
IDs. At this checkpoint, 3,722 packages are locally complete and remotely
verified, package authoring has reached the permanent frontend-ID ceiling of
4005, and every package has a remotely verified Optimal submission. The generated
migration reports in
[`dsa/leetcode/_reports/`](dsa/leetcode/_reports/) are the current source of
truth. In particular, the generated
[`END_OF_CORPUS_REWORK_GAPS.md`](dsa/leetcode/_reports/END_OF_CORPUS_REWORK_GAPS.md)
currently records all 283 packages that are not fully complete (zero active
verified-solution scaffolds and 283 deferred documentation-only failures), all
3,285 packages whose source fidelity has not yet been reviewed, and 15 known
repository-regression packages for the consolidated cleanup pass.

The fixed objective is one complete educational package for each of those
4,005 indexed problems. Frontend ID 4005 is the permanent application boundary;
future LeetCode publications will not expand this corpus.

LeetCode-derived metadata is also frozen. The final authenticated snapshot was
captured on **2026-07-29** and includes the then-current official difficulty,
acceptance rate, Premium Frequency, and every bundled company/list relevance
signal. Those values are historical snapshots, not claims about current or
future company interview activity. Real contest Elo comes from the final
[ZeroTrac](https://zerotrac.github.io/leetcode_problem_rating/#/) snapshot;
problems absent from ZeroTrac retain an explicitly labelled estimated Elo.
Neither source will be refreshed for this application after the freeze date.

## How a problem package is organized

Each problem has one canonical home:

```text
dsa/leetcode/<frontend_id:04d>_<slug>/
  metadata.json
  doc.md                              # legacy document or compatibility anchor
  reference/                          # section-authored Reference document
    description.md
    contract.md
    examples.md
    constraints.md
    follow_up.md                      # optional source-native section
  source_fidelity.json                # optional reviewed source-fidelity facts
  cases.json
  benchmark.json
  guided_example.md                 # optional code-free worked example
  solution_variants.json           # Optimal-first branch manifest
  variants/
    optimal/
      approach.md
      submission.json              # present after remote verification
      solutions/
        solve.py                    # app-local Python solve(...) implementation
        leetcode.py                 # native candidate when available
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

VS Code 1.121 and newer render fenced `mermaid` blocks directly in the built-in
Markdown preview. Open a package Markdown file and press `Ctrl+K V` to preview
beside the editor, or `Ctrl+Shift+V` to replace the editor with the preview. No
extension is required. If a preview opened before a VS Code update still shows
the Mermaid source as an ordinary code block, close and reopen the preview (or
reload the VS Code window) and verify that the file language is Markdown and
the built-in **Markdown Language Features** extension is enabled.

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
npm.cmd run test:mermaid --prefix web
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
