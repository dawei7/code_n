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
- The canonical application corpus ends permanently at frontend ID 4005 and
  contains exactly 4,005 packages once that final import is present. Never add
  frontend ID 4006 or later, even when LeetCode publishes more problems; all
  import and refresh workflows must preserve this frozen ceiling.
- The installed application is offline-first. Canonical resources are
  read-only; progress and personal solutions must be written to Electron's
  user-data directory.
- The editor, runner, and debugger are in-app workflows. Do not make an
  external IDE a requirement.
- English is the only natural language for the product, canonical learning
  content, generated reports, and user interface. Do not add translation
  files, locale selectors, or translated-document fallbacks.
- The desktop app preloads canonical challenge summaries once before reporting
  health. Set selectors must filter that in-memory corpus client-side and must
  never clear or refetch the list during a view change.
- `npm run dev` must use the Vite development server directly; do not put a
  production web build on the interactive development startup path.

## Sources of truth

1. The current worktree and tests.
2. `dsa/leetcode/index.json`, `dsa/leetcode/subsets.json`, and each package's
   `metadata.json`.
3. Authored `cases.json`, complexity verification (`benchmark.json` or a
   strictly validated `complexity_certificate.json`), and package solutions.
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
- The desktop app preloads canonical challenge summaries once before reporting
  health. Set selectors must filter that in-memory corpus client-side and must
  never clear or refetch the list during a view change.
- `npm run dev` must use the Vite development server directly; do not put a
  production web build on the interactive development startup path.

## Sources of truth

1. The current worktree and tests.
2. `dsa/leetcode/index.json`, `dsa/leetcode/subsets.json`, and each package's
   `metadata.json`.
3. Authored `cases.json`, complexity verification (`benchmark.json` or a
   strictly validated `complexity_certificate.json`), and package solutions.
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
  doc.md                    # legacy document or section-mode compatibility anchor
  template.<ext>            # exact LeetCode code editor starter template (e.g. template.py)
  reference/                # optional section-authored Reference document
    follow_up.md            # optional source-native section
  source_fidelity.json      # optional reviewed structure and factual evidence
  cases.json
  benchmark.json             # normal complexity-verification path
  complexity_certificate.json # only when legal scaling is inapplicable
  guided_example.md           # optional code-free representative walkthrough
  solution_variants.json     # required branch manifest; Optimal is default
  assets/                   # optional package-local doc assets
  variants/
    optimal/
      approach.md
        solutions/
          solution.<ext>         # primary-language solution (solution.py, solution.js, solution.sql, solution.sh)
    simplified/                  # optional, legacy fallback
      submission.json
      solutions/
```

- `server/app/challenge_packages.py` is the path API for these packages.
- Guided examples are package-authored Markdown lessons served by
  `/api/docs/by-id/{challenge_id}/guided-example`. Each lesson works through
  one representative input step by step using precise prose, mathematical
  notation, Markdown tables or diagrams, and optional package-local images.
  The lesson must teach the reasoning and expose material traps without showing
  solution code or pseudocode.
- `GUIDED_EXAMPLES.md` is the format and authoring authority. Do not add a step
  manifest, playback state, renderer-specific UI, semantic code anchors, or a
  second solution explanation. The package's `guided_example.md` is the sole
  source for this teaching surface.
- Reference and Guided Example PDF exports use Electron's native Save As dialog
  and a dedicated A4 print document. Keep exported PDFs light-only regardless
  of the active app theme, expand printable instructional content, omit locked
  solutions and UI controls, and preserve left-aligned display mathematics.
- Canonical package prefixes are zero-padded to four digits for numeric
  filesystem ordering. This formatting does not change metadata frontend IDs,
  challenge IDs such as `lc_1`, official URLs, or user-data identities.
  Only after LeetCode reports Accepted may the staged source replace the
  canonical native file and the manifest be updated with that submission's id
  and timestamp.
- During canonical migration, follow the early-verification authoring order in
    simplified/              # optional; authored in a later reviewed pass
      approach.md
      submission.json
      solutions/
```

- `server/app/challenge_packages.py` is the path API for these packages.
- Guided examples are package-authored Markdown lessons served by
  `/api/docs/by-id/{challenge_id}/guided-example`. Each lesson works through
  one representative input step by step using precise prose, mathematical
  notation, Markdown tables or diagrams, and optional package-local images.
  The lesson must teach the reasoning and expose material traps without showing
  solution code or pseudocode.
- `GUIDED_EXAMPLES.md` is the format and authoring authority. Do not add a step
  manifest, playback state, renderer-specific UI, semantic code anchors, or a
  second solution explanation. The package's `guided_example.md` is the sole
  source for this teaching surface.
- Reference and Guided Example PDF exports use Electron's native Save As dialog
  and a dedicated A4 print document. Keep exported PDFs light-only regardless
  of the active app theme, expand printable instructional content, omit locked
  solutions and UI controls, and preserve left-aligned display mathematics.
- Canonical package prefixes are zero-padded to four digits for numeric
  filesystem ordering. This formatting does not change metadata frontend IDs,
  challenge IDs such as `lc_1`, official URLs, or user-data identities.
  Only after LeetCode reports Accepted may the staged source replace the
  canonical native file and the manifest be updated with that submission's id
  and timestamp.
- During canonical migration, follow the early-verification authoring order in
  `LEETCODE_SUBMISSIONS.md`: confirm contract and native interface, minimally
  sanity-check the exact native source, obtain remote Accepted evidence, then
  use that accepted source to anchor the app-local adapter, comprehensive
  correctness cases, and complexity calibration. If a later rejection or
  source change exposes a semantic misunderstanding, revise documentation,
  cases, expected outputs, both solution forms, and affected benchmark claims
  together, then rerun every gate.
- **`solve.*` TEMPLATE & HARNESS STRUCTURE**:
  - Anything placed **outside** of `solve(...)` or `Solution` at the top level of `solve.*` (such as helper classes `ListNode`, `TreeNode`, `Employee`, `Master`, `GuessGame`, or API stubs like `read4`) constitutes the **platform-provided template / harness**.
  - The user is NOT expected to implement or recreate these platform-provided helper structures. They are provided as part of the starter environment just like on LeetCode.
  - The user's task is strictly confined to the solution function/class itself (`Solution` / `solve`).
  - All platform-provided helpers and API stubs must be cleanly declared at the module level outside `solve(...)`, ensuring full type-hinting and zero IDE/linter warnings (no red squiggly lines).

## Active accelerated solution-and-Reference campaign

`SOLUTION_QUALITY.md` owns the default ongoing corpus campaign. Complete
Premium packages first and exclusively, processing one package at a time in
ascending frontend-ID order. Finish an already-started package before returning
to the recomputed queue head.

A Premium package is complete for this campaign only when all four conditions
hold in the same package pass:

1. The Optimal solution has a current, hash-bound expert-quality review.
   Accelerated reviews created from this point forward use `review_scope` equal
   to `solution_only`; an earlier current `solution_and_cases` review still
   satisfies the solution dimension, while its case status is ignored.
2. The complete `variants/optimal/approach.md` has been reviewed against that
   solution or its inert candidate and accurately teaches its algorithm, data
   flow, correctness, complexity, alternatives, and material edge cases.
3. The package uses the modular `reference/` structure.
4. `source_fidelity.json` validates as `verified` against authoritative live
   source evidence.

Case-quality completion and benchmark calibration are explicitly deferred to a
separate future campaign. Do not proactively inspect, expand, rewrite,
reclassify, calibrate, or review `cases.json` or `benchmark.json`; do not create
`case_review` evidence or claim case-quality completion. Keep every
`benchmark.json` byte-for-byte unchanged. Treat a bound benchmark hash only as
inherited artifact identity, never as evidence of a fresh calibration review.
When no candidate is created, do not run or analyze that package's cases or
benchmarks during this campaign.

Create `candidate.<extension>` only when it materially improves the protected
app-local solution under the expert-interview standard in
`SOLUTION_QUALITY.md`. Keep every candidate inert: never promote it, submit it,
or represent it as remotely Accepted. Preserve good protected solutions,
verified app/native sources, `submission.json`, metadata, and
`solution_variants.json` exactly unless a separately proven defect authorizes a
change. When a candidate is created, run the existing unchanged judge only as
a black-box compatibility gate. Inspect only an ordinary case that the
candidate fails, and delete it only when authoritative source evidence
independently proves the case wrong; never add a replacement. Do not inspect or
modify a failed benchmark. Leave such a candidate inconclusive or omit it and
preserve the protected solution.

Derive the Premium queue from current solution-quality completion plus verified
source fidelity, ignoring case-quality status. After each completed package,
run its direct validators and protected-file integrity checks. Run the complete
dataset audit without `--solution-only` and
`tools/audit_leetcode_migration.py` after every fifty campaign completions and
once more before session handoff, then reopen the refreshed reports and
recompute the queue. `first_unverified_optimal_submission` remains an integrity
signal for remote Accepted evidence, not the active campaign queue.

For each active package, author `reference/description.md`, `contract.md`,
`examples.md`, `constraints.md`, and every additional source-native section;
retain `doc.md` only as the composition anchor. Verify Premium statements
through the authenticated read-only Chrome source workflow (`browser_subagent`).
**MANDATORY LIVE SOURCE FETCH**: For EVERY problem package, the agent MUST first run `browser_subagent` to open `https://leetcode.com/problems/<slug>/description/`, extract the full live statement (including all Markdown schema tables, interface declarations, math formulas, notes, hints, and example tables), and extract the exact starter template from the LeetCode code editor (including all docstrings, comments, parameter types, and method signatures verbatim with an indented `pass` inside function bodies to prevent syntax and linter errors), saving it as `template.<ext>` (e.g. `template.py` or `template.sql`) in the root of the problem package directory. Never draft `reference/` files or starter code from unverified local summaries. Preserve every source schema, example, explanation, constraint, note, hint, table, diagram, and other source-native section without copying provider prose or HTML. Direct source evidence is mandatory for a verified fidelity manifest: if it is unavailable, keep the package in progress and do not move to another package.

**UNIVERSAL PRESERVATION OF EXACT CONTRACTS, SCHEMAS & TECHNICAL FACTS**: Across ALL DSA categories (Algorithms, Data Structures, Trees, Graphs, Strings, Math, SQL/Database):
- Never omit, abbreviate, or alter essential source declarations, table schemas, primary/foreign key designations (e.g. `primary key (column with unique values)`), custom class/interface code blocks (e.g. `interface FontInfo`, `class Node`), method contracts, parameter ranges, return guarantees, edge-case constraints, notes, hints, or mathematical expressions.
- Preserve every source schema, table, code interface block, LaTeX equation, constraint, note, hint, and follow-up in its original logical position.
- Rephrase surrounding narrative prose for independent clarity, but keep all technical definitions, variable names, literals, and structural guarantees strictly intact.

**STRICT MINIMAL MODIFICATION & 1:1 LIVE FIDELITY RULE**:
- Copy live source narrative, technical definitions, math relations, variable names, indices, interface blocks, table schemas, and structural facts 1:1. Rephrase or edit text ONLY when necessary to improve clarity; never add custom narrative padding or arbitrary rephrasings. Under the requirement to copy 1:1 without unnecessary rephrasing or custom narrative padding, `0253_meeting-rooms-ii` is the first package where rephrasing occurred; agents must never deviate from 1:1 live source fidelity.
- NEVER alter variable identifiers (e.g. keep uppercase $A$, $B$, index $i$ as in the source; do not change $A$ to lowercase `a` or remove index $i$), mathematical expressions (e.g. keep $A[i] \neq B[i]$ and $A[i] > B[i]$), literals, or index notation.


## Documentation

- `README.md` is served by `/api/docs/overview` and packaged with the app.
- Per-problem documentation exists only inside its canonical
  `dsa/leetcode/<frontend_id:04d>_<slug>/` package. Legacy packages use
  `doc.md`; section-authored packages use `reference/description.md`,
  `contract.md`, `examples.md`, and `constraints.md`, with `doc.md` retained
  only as a compatibility anchor during migration.
- Mathematical explanation belongs in the canonical problem document; there
  is no separate mathematical-doc tree or tab.
- Do not create a parallel `docs/algorithms`, `docs/mathematical`, provider, or
  subset tree.
- Write original summaries. Do not copy full LeetCode statements, editorials,
  or proprietary solution text.
- A complete problem document should state the contract, give clear examples,
  explain underlying algorithms, and provide time/space complexity without
  leaking the full answer unless that artifact intentionally contains it.
- Follow `dsa/leetcode/_template.md` for legacy documents. In section mode, use
  `Description`, `Function Contract`, `Examples`, and `Constraints` in that
  order, with one matching level-two heading per file. The server generates the
  metadata table and its sole official `LeetCode` link when it composes those
  files. Add source-native sections such as `Follow-up` after `Constraints`
  when the live statement contains them. Do not repeat an external link in a
  reference section.
- Source fidelity is a separate review dimension from package completion. A
  package is only source-fidelity verified when its `source_fidelity.json`
  passes `tools/leetcode_source_fidelity.py`; a missing manifest means
  unverified, not implicitly correct. The manifest stores statement structure,
  factual example literals, counts, review assertions, and a live-content hash,
  never the provider's prose or HTML. The review also hashes every composed
  local section file so later edits invalidate verification until the package
  is reviewed again.
- Preserve every source example in the same order with the same input and
  output facts. Preserve whether each example has an explanation and rephrase
  that explanation without dropping any reasoning step or material detail. Do
  not invent replacements or normalize every problem to three examples. Put
  genuinely useful additions under a separately labelled `Additional Examples`
  section, never inside the canonical source example sequence.
- Preserve every constraint, note, follow-up, list, and other source-native
  section in its original logical position. Recreate tables with the same data
  and schema in Markdown. For source images or diagrams, create an independent
  local diagram or an equivalently complete accessible table; do not copy the
  provider asset. Record source and local visual/table counts in the fidelity
  manifest and manually verify their informational equivalence.
- Preserve source presentation when it carries meaning: the same signpost
  sequence, comparable paragraph depth, example grouping, explanatory steps,
  table columns and rows, diagram relationships, notes, and material emphasis.
  This is structural and pedagogical fidelity, not cosmetic imitation. Do not
  copy provider prose, HTML, CSS, icons, or branding, and do not claim that an
  independently written Reference is verbatim. A Reference can be
  source-fidelity verified only when it is both factually accurate and
  equivalently clear and extensive.
- Use fenced `mermaid` blocks for graph, tree, flow, and relationship diagrams
  that Mermaid can express clearly. Every block must include `accTitle` and
  `accDescr`, must rely on the app's site-level theme and security settings
  rather than per-diagram initialization, and must remain understandable from
  the surrounding prose. Layout-only frontmatter may tune `flowchart.padding`,
  `nodeSpacing`, and `rankSpacing` when the default geometry is not readable in
  both the app and VS Code preview; do not override the site theme or security
  level. The Reference, Guided Example, and PDF renderers share this path. Run
  `npm.cmd run test:mermaid --prefix web` after adding or editing a diagram.
  Reserve package-local images for visuals Mermaid cannot represent faithfully.
- Do not add Required Complexity, Approach, Solution, or Reference
  Implementations to the shared problem document or its section files. Branch
  artifacts live under `variants/<id>/`.
- Required Complexity belongs to each row of `solution_variants.json` and is
  rendered inside the selected top tab. The corresponding explanation lives in
  `variants/<id>/approach.md`. Do not duplicate either section in `doc.md` or
  `reference/`.
- Give `Goal` in legacy documents, or `Description` in section-authored
  documents, an original, source-faithful problem narrative with depth and
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
  material boundary condition. Keep exact technical terms, literals, and
  mathematical facts, but independently write expressive prose. Never compress
  a rich statement into a one-sentence summary.
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
  bound appears. When the underlying expression is long or would be repeated,
  prefer a displayed definition such as:

  $$
  S = \sum_{w \in \texttt{words}} \lvert w \rvert.
  $$

  Then use the short symbol `$S$` in the prose and complexity bounds.
- Keep each manifest's `time_complexity` and `space_complexity` as plain
  `O(...)` notation. The UI renders them as exactly two Required Complexity
  bullets. Put qualifications such as expected hash behavior and the meanings
  of variables in `Complexity detail`, never in the manifest bound.
- Each branch's `Approach` is collapsible. Make it maximally educational and
  specific to the problem: derive the algorithm from its constraints and use
  precise algorithm/data-structure terms. Every branch `approach.md` must
  contain exactly three level-two headings, in this order: `General`,
  `Complexity detail`, and `Alternatives and edge cases`. Do not add any other
  Markdown headings inside `approach.md`. `General` is a container, not a
  requirement to write one
  unbroken block: use descriptive bold subheadings such as
  `**Why the unique pair must be found**` whenever they make the problem's
  distinct ideas easier to navigate. These bold subheadings must be
  problem-specific and optional, never another repeated mini-template. Put the
  problem-specific derivation and correctness reasoning under `General`. Do not
  mechanically copy Two Sum's sequence or force an invariant, trace,
  correctness proof, or fixed number of points when that structure does not
  improve the explanation. Explain why the method is correct within the
  derivation; never use `Correctness`, `Correctness argument`, or comparable
  generic proof slots. `0001_two-sum/variants/optimal/approach.md` is a
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
.\.venv\Scripts\python.exe tools\audit_leetcode_source_fidelity.py
.\.venv\Scripts\python.exe -m pytest server\tests\test_dynamic_docs.py -q
```

The source-fidelity audit defaults to the currently reviewed low-ID batch. For
a newly completed higher-ID package, also run it with
`--max-frontend-id <completed-id>` or validate that package directly; never
mistake exclusion from the default scope for successful review.

After each Premium package, run its direct validators and integrity checks and
rederive the accelerated queue from live solution-review and source-fidelity
evidence. Refresh the complete dataset and migration reports after every fifty
campaign completions and before session handoff. Ignore case-quality status
when choosing work for this campaign.

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
- Scaling remains the default and preferred complexity-verification method. A
  package may use `complexity_certificate.json` only when its complete legal
  source domain is bounded too tightly for an honest scaling verdict, when a
  fixed concurrency contract is verified through safety/progress evidence, or
  when a problem-level lower bound matches the required upper bound and no
  genuine principal slower class exists.
- A certificate must pass `engine/complexity_certificates.py`, use one of the
  reviewed methods `bounded_domain`, `bounded_concurrency`, or
  `asymptotic_optimality`, and record the required replacement evidence. It is
  not a generic waiver and must not coexist with a completed scaling benchmark.
- Certified packages still require every ordinary correctness case, the
  optimal app-local reference, the separate native artifact, remote Accepted
  verification, and certificate-specific regression tests. Real-test and the
  UI must identify the certificate method explicitly and must never describe
  it as a measured runtime verdict.
- If any of the original eighteen complexity blockers (frontend IDs 401, 405,
  479, 999, 1108, 1114-1118, 1134, 1137, 1154, 1165, 1188, 1195, 1226, or
  1242) reappears, read
  `dsa/leetcode/_reports/ORIGINAL_18_BLOCKER_PLAYBOOK.md` completely. It owns
  the reviewed per-ID benchmark-versus-certificate routing, shared concurrency
  runtime prerequisites, regression evidence, and blocker-clearing procedure.
  Do not reclassify those packages from an old chat summary.

## Frozen LeetCode metadata and the final corpus import

`LEETCODE_METADATA.md` is authoritative for Frequency, estimated Elo, and
newly published problem imports. Read it before changing these fields.

- LeetCode metadata is frozen as of 2026-07-29. Do not refresh official
  difficulty, acceptance, Premium Frequency, company/list relevance,
  ZeroTrac ratings, or estimated Elo unless the user explicitly replaces the
  freeze policy.
- Treat every bundled company signal as a historical snapshot, never as a
  claim about current or future company interview relevance.
- The final refresh used the authenticated 4,005-row LeetCode snapshot and
  ZeroTrac revision `a99138e145f303597b85290519aaf3d219b3a3e7` (2,545 real
  ratings, upstream updated 2026-07-24). The other 1,460 values are explicitly
  estimated.
- Import only frontend IDs absent from the canonical index through the
  permanent frontend-ID ceiling of 4005 with:
  `.\.venv\Scripts\python.exe tools\import_new_leetcode_problems.py`
- Once the index contains all 4,005 packages, treat that command as a freeze
  audit: it may report later upstream IDs, but it must never create a package
  or index entry above 4005.
- Never hand-edit `frequency`, `elo_rating`, or `estimated_elo_rating`. The
  historical updater validates the complete source corpus before atomically
  writing package metadata and the index. Real and estimated Elo are mutually
  exclusive in each problem record.
- LeetCode Frequency requires a valid signed-in Premium session. An expired or
  non-Premium session must fail without replacing values with zeros.
- The Elo set remains real ZeroTrac-only. Estimated Elo is for display,
  navigation, and direct problem-level averages, never set membership.

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
- Generated starter signatures must come from the executable contract: prefer
  the authored app-local `solve(...)` signature, then authored `cases.json`
  input keys. Never infer parameters from unconstrained prose bullets.
- LeetCode may show source-native models such as `TreeNode`, `ListNode`, `Node`,
  or `Point` as comments because its judge injects them. An app-local Python
  reference that uses such a model must define the minimal class explicitly,
  mark it with a `Local equivalent of ...` class docstring, and include it in
  the generated editable user starter. Never rely on an invisible runner
  global or hide an undefined model name with `# noqa: F821`; runner injection
  exists only for backward compatibility with already saved user files.
- Under `Function Contract` -> `Inputs`, format only real parameters as
  ``- `name`: ...`` entries. Put shared constraints and semantic notes in
  paragraphs or subordinate prose so they cannot be mistaken for parameters.
- Any starter-generation change must keep the global contract regression in
  `tests/test_solution_templates.py` green; it compares generated parameters
  with app-local solution signatures and authored case inputs.
- Never write user files into packaged `resources/dsa/leetcode`.
- Never commit `.coden-data` or another user's app-data files.
- Preserve existing solution contents during storage migrations and verify
  hashes before removing a legacy path.

## Language and runtime contracts

Language metadata is centralized in `engine/languages.py`.

- Each problem exposes exactly one user-facing language, derived from its
  verified LeetCode submission and normalized to Python, JavaScript, SQL, or
  Bash. Do not expose alternate-language editors or reference solutions.
- Legacy runner implementations and personal solution files for other
  languages may remain internally for compatibility, but they are not
  user-facing language choices and must not be deleted during this migration.
- Python and JavaScript use function-call harnesses where the challenge
  supports them.
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
