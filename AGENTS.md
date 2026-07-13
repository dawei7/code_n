# cOde(n) Agent Guide

This file is the authoritative repository-local guide for coding agents. It
applies to the entire checkout. Read the live worktree before acting: generated
reports, package metadata, and user changes can be newer than any conversation
or external memory.

## Product invariants

- cOde(n) is LeetCode-based. Do not recreate GeeksforGeeks, CodeChef, or
  standalone NeetCode challenge roots.
- NeetCode, AlgoMaster, company lists, study plans, topics, and tags are views over the
  canonical LeetCode packages, never copied challenge datasets.
- Preserve LeetCode identity: numeric frontend id, title slug, official URL,
  supported language, category, and source-native execution semantics.
- The installed application is offline-first. Canonical resources are
  read-only; progress and personal solutions must be written to Electron's
  user-data directory.
- The editor, runner, and debugger are in-app workflows. Do not make an
  external IDE a requirement.
- The desktop app preloads canonical challenge summaries once before reporting
  health. Set selectors must filter that in-memory corpus client-side and must
  never clear or refetch the list during a view change.
- `npm run dev` must use the Vite development server directly; do not put a
  production web build on the interactive development startup path.

## Sources of truth

1. The current worktree and tests.
2. `dsa/leetcode/index.json`, `dsa/leetcode/subsets.json`, and each package's
   `metadata.json`.
3. Authored `cases.json`, `benchmark.json`, and package solutions.
4. `dsa/leetcode/_reports/_completion_report.json` for the current doc queue.
5. This `AGENTS.md` for repository workflow and invariants.
6. `README.md` for the public/product overview and developer quick start.
7. `RELEASING.md` for Windows signing, release, and update procedures.

Do not treat old chat summaries, cached counts, or external agent memory as
more authoritative than the live files above. Codex may also have user-level
memory outside the repository; that is contextual history, not project source.

## Architecture

- `engine/`: reusable Python engine types, language metadata, tracing,
  complexity logic, progress models, and starter generation.
- `challenges/`: registry and dynamic LeetCode `AlgorithmSpec` adapter.
- `dsa/leetcode/`: canonical problem packages and subset metadata.
- `server/`: FastAPI API, execution harnesses, DAP debugger bridge, user-data
  storage, validation, and packaged server entrypoint.
- `web/`: React, TypeScript, Vite, Monaco, Zustand, reference UI, runtime
  analysis, cases, and debugger interface.
- `electron/`: Windows desktop shell, user-data selection, updates, and
  packaging configuration.
- `tools/`: dataset checks, synchronization, validation, and developer CLIs.

The repository folder may still be named `code_n`; the import package is
`engine`. All Python imports must use the `engine` namespace, never the former
inner-package namespace.

## Canonical challenge package

Each problem is stored once:

```text
dsa/leetcode/<frontend_id:04d>_<slug>/
  metadata.json
  doc.md
  doc_de.md                 # optional translation
  cases.json
  benchmark.json
  submission.json            # optional verified LeetCode submission manifest
  assets/                   # optional package-local doc assets
  solutions/
    python.py               # canonical app-friendly reference
    <language>.<extension>  # optional same-language references
    leetcode_<lang>.<ext>   # optional platform-native submission candidate
```

- `server/app/challenge_packages.py` is the path API for these packages.
- Canonical package prefixes are zero-padded to four digits for numeric
  filesystem ordering. This formatting does not change metadata frontend IDs,
  challenge IDs such as `lc_1`, official URLs, or user-data identities.
- `challenges/algorithms/leetcode.py` loads packages into the registry.
- External practice lists remain views: AlgoMaster membership and pattern order
  live in `dsa/leetcode/_meta/algomaster-subsets.json` and are refreshed with
  `tools/sync_algomaster_subsets.py`; they never create duplicate packages.
- `_local/` is private and ignored. Do not package it.
- `_reports/` is generated workflow state; do not hand-edit derived counts.
- Reference solutions are not personal attempts. When official submit-ready
  LeetCode forms are added, keep them beside—not instead of—the app-adapted
  `solve(...)` form and preserve original declarations.
- `LEETCODE_SUBMISSIONS.md` is authoritative for direct submission. A package
  candidate must remain blocked until the exact source is remotely Accepted and
  its manifest is promoted to `verified`; never infer verification from local
  correctness alone.

## Documentation

- `README.md` is served by `/api/docs/overview` and packaged with the app.
- Per-problem documentation exists only at
  `dsa/leetcode/<frontend_id:04d>_<slug>/doc.md`.
- Mathematical explanation belongs in the canonical problem document; there
  is no separate mathematical-doc tree or tab.
- Do not create a parallel `docs/algorithms`, `docs/mathematical`, provider, or
  subset tree.
- Write original summaries. Do not copy full LeetCode statements, editorials,
  or proprietary solution text.
- A complete problem document should state the contract, give clear examples,
  explain underlying algorithms, and provide time/space complexity without
  leaking the full answer unless that artifact intentionally contains it.
- Follow `dsa/leetcode/_template.md`. The metadata table owns the only official
  problem link and labels it `LeetCode` so the UI renders a clickable LeetCode
  symbol. Do not repeat an external link below `Problem Description`.
- Use `Goal`, `Function Contract`, `Examples`, and `Required Complexity` in that
  order. Do not add a `Solution` or `Reference Implementations` section to the
  problem document; implementation artifacts live in the package's `solutions/`
  directory.
- Give `Goal` an original, source-faithful problem narrative with depth and
  length proportionate to the public statement. Follow the original problem's
  logical order as closely as independent wording permits: introduce the same
  scenario or data model, state every operation rule and guarantee that affects
  interpretation, preserve distinctions and boundary semantics, and finish
  with the exact requested outcome. Use multiple paragraphs when the source has
  substantial context. Rephrase all prose rather than copying LeetCode's text;
  fidelity means complete semantic coverage, not sentence-level imitation or
  generic padding. Preserve source-native technical vocabulary exactly: do not
  replace terms such as `ascending`, `non-decreasing`, `strictly increasing`,
  `subarray`, `subsequence`, `at most`, or `exactly` with near-synonyms. Rephrase
  surrounding sentences, not mathematical relations or named concepts. Do not
  rewrite merely to make the prose different: every departure from the source
  should improve clarity, sequencing, semantic coverage, or explanation of a
  material boundary condition. Keep source wording and structure when they are
  already the clearest independently usable formulation. Never compress a rich
  statement into a one-sentence summary.
- Write mathematical expressions as LaTeX using `$...$` inline or `$$...$$`
  for a display equation. Use conventional notation such as `\lvert x \rvert`,
  `\lfloor x \rfloor`, `\lceil x \rceil`, `\min`, `\max`, `\sum`, and
  `\log`. Keep executable calculations in code spans, including assignments,
  array or map indexing, slices, function calls, pointer updates, and
  language operators; for example, write `nums[a] = target - nums[b]`, not a
  LaTeX rendering of that computation. Keep backticks as well for identifiers
  discussed as code, strings, serialized inputs and outputs, SQL, and other
  literal data. Use LaTeX for abstract relations, proofs, combinatorics,
  geometry, probability, summations, and complexity bounds, with ordinary
  mathematical symbols instead of code-styled identifiers. When a compact
  complexity bound uses a problem-specific quantity, define that symbol in
  `Function Contract` or the surrounding non-collapsed explanation before the
  bound appears.
- Keep `Required Complexity` notation-only, with exactly these two bullets:
  `- **Time:** $O(...)$` and `- **Space:** $O(...)$`. Put qualifications and
  the meanings of variables in `Complexity detail`, not beside the bounds.
- Only `Approach` is collapsible. Make it maximally educational and specific to
  the problem: derive the algorithm from its constraints and use precise
  algorithm/data-structure terms. Every Approach must contain exactly three
  level-four subsection headings, in this order: `General`, `Complexity detail`,
  and `Alternatives and edge cases`. Do not add any other Markdown headings
  inside Approach. `General` is a container, not a requirement to write one
  unbroken block: use descriptive bold subheadings such as
  `**Why the unique pair must be found**` whenever they make the problem's
  distinct ideas easier to navigate. These bold subheadings must be
  problem-specific and optional, never another repeated mini-template. Put the
  problem-specific derivation and correctness reasoning under `General`. Do not
  mechanically copy Two Sum's sequence or force an invariant, trace,
  correctness proof, or fixed number of points when that structure does not
  improve the explanation. Explain why the method is correct within the
  derivation; never use `Correctness`, `Correctness argument`, or comparable
  generic proof slots. `0001_two-sum/doc.md` is a
  quality exemplar, not a mandatory prose schema. Match depth to difficulty: concise reasoning is
  appropriate for a genuinely simple observation, while complex algorithms
  must receive longer derivations, state definitions, transitions, examples,
  and proofs as needed. Do not shorten an explanation merely to keep documents
  uniform. Write `Alternatives and edge cases` as a scannable bullet list, not
  free-text paragraphs. Name each alternative in bold followed by a colon, for
  example `- **Visited matrix plus direction changes:** ...`, and state its
  tradeoff or failure mode. Follow with separate bullets for material boundary
  conditions and semantic traps. The problem determines the number of bullets;
  do not force a fixed count or shorten explanations merely to make them
  visually uniform.

For dataset documentation work:

```powershell
.\.venv\Scripts\python.exe tools\check_leetcode_dataset.py
.\.venv\Scripts\python.exe -m pytest server\tests\test_dynamic_docs.py -q
```

Always reopen the refreshed completion report before selecting the next batch.

## Runtime benchmark authoring

`BENCHMARKING.md` is the benchmark and complexity-verdict specification.
`dsa/leetcode/0001_two-sum/benchmark.json` is the reviewed package exemplar.

- Keep runtime workloads in `benchmark.json`, never in the ordinary case file.
- Two tiers are the minimum for scaling; author three when migrating a package.
- Use positive, unique, increasing `size` values with at least a 4x total span.
- Define `size` as the workload variable governing the required complexity and
  keep that meaning consistent across tiers.
- Exercise the complexity-sensitive path without changing the problem's
  semantics or expected result.
- Verify a correct slower-class implementation passes every output and fails
  only the complexity verdict. A benchmark safety-cap failure must not be
  misreported as an incorrect hidden answer when the implementation can
  reasonably complete under the larger benchmark allowance.
- Do not copy Two Sum's sizes mechanically. Every problem needs authored inputs
  appropriate to its constraints, likely slower alternative, and runtime.
- Preserve the legacy one-tier 1.5x rule until a package is intentionally
  migrated; do not silently infer tiers from ordinary cases.

## Personal solutions and progress

Development user data lives under ignored `.coden-data/`. Installed user data
lives under Electron `app.getPath('userData')`.

```text
<user-data>/
  progress.json
  dsa/leetcode/<frontend_id>_<slug>/user_solutions/
    python_v1.py
    python_v2.py
    python_v3.py
    versions.json
```

- Every supported language uses exactly v1, v2, and v3 files.
- User-data problem folders intentionally retain unpadded logical frontend IDs
  for compatibility with existing profiles; only canonical repository package
  folders use four-digit prefixes.
- There is no unversioned active alias. `versions.json` selects the active
  file and stores optional display names.
- `server/app/user_solutions.py` owns path resolution and legacy migration.
- Never write user files into packaged `resources/dsa/leetcode`.
- Never commit `.coden-data` or another user's app-data files.
- Preserve existing solution contents during storage migrations and verify
  hashes before removing a legacy path.

## Language and runtime contracts

Language metadata is centralized in `engine/languages.py`.

- Python, C++, Java, C#, JavaScript, Go, and Kotlin use function-call harnesses
  where the challenge supports them.
- SQL receives authored table fixtures and runs in an isolated database.
- pandas is Python with DataFrames created from authored table fixtures.
- Bash receives raw stdin and package-authored files in a temporary directory.
  Keep values such as `"3\n"` as raw stdin; never reframe them as function
  arguments.
- Concurrency problems may be tracked but are not automatically runnable unless
  metadata and a real runtime explicitly support them.

Relevant implementations:

- `server/app/engine_runner.py`
- `server/app/external_programs.py`
- `server/app/special_environments.py`
- `server/app/validated_cases.py`
- `server/app/routes/run.py`
- `server/app/routes/debug.py`
- `server/app/dap_client.py`

Runtime overrides include `CODEN_CPP_COMPILER`, `CODEN_JAVAC`, `CODEN_JAVA`,
`CODEN_DOTNET`, `CODEN_NODE`, `CODEN_GO`, `CODEN_KOTLINC`, `CODEN_BASH`, and
`CODEN_DEBUG_TOOLS_DIR`.

## Verification

Use the repository virtual environment on Windows; the shell Python may lack
test dependencies. Use `npm.cmd` when PowerShell blocks `npm.ps1`.

Core validation:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
npm.cmd run build --prefix web
npm.cmd run build --prefix electron
```

Useful focused checks:

```powershell
.\.venv\Scripts\python.exe -m pytest server\tests -q
.\.venv\Scripts\python.exe -m pytest tests -q
.\.venv\Scripts\python.exe -m ruff check engine server challenges tools tests
git diff --check
```

Installed-runtime changes also require proportionate packaging validation:

```powershell
.\.venv\Scripts\python.exe build_app.py --step server
cd electron
npx.cmd electron-builder --win --x64 --dir --publish never
```

Smoke-test the frozen server with separate `CODEN_HOME` and `CODEN_DSA_DIR`
paths. Confirm it can load challenges, create user version files outside
resources, and serve the packaged overview/reference docs.

## Change discipline

- Preserve unrelated dirty-worktree changes; inspect `git status` before and
  after broad refactors.
- Use `rg`/`rg --files` for discovery and `apply_patch` for text edits.
- Update imports, tests, PyInstaller hidden imports, Electron resources, UI
  labels, comments, and developer tools together when a path changes.
- Prefer focused tests while iterating, then run the full suite before handoff.
- Do not delete or move user data without verifying the resolved absolute path
  and confirming the replacement contains the same information.
- Do not commit, push, publish, alter `main`, or create releases unless the user
  explicitly authorizes that external change.
- Do not report completion while required tests/builds are failing or a package
  still depends on a removed legacy path.

## Release authority

Follow `RELEASING.md` and `release.py`. Windows releases must account for code
signing, SmartScreen reputation, child-process shutdown before updates, and
verification of the actual packaged artifact. Do not infer release readiness
from source tests alone.
