# Active LeetCode Migration Handoff

Updated: 2026-07-13

This work is active and neither complete nor globally blocked. The full goal
remains active.

## Goal

Migrate every canonical LeetCode package in `C:\dawei7\code_n`, in numeric
frontend-ID order from problem 1 through the current final problem 3985, to the
reviewed Two Sum standard. Each completed package needs an original `doc.md`,
authored correctness cases, three ordered complexity-sensitive benchmark tiers,
an optimal app-local solution for every runnable supported environment, a
platform-native LeetCode submission artifact in Python 3 or the problem's
required restricted language, remote Accepted verification where access and
execution semantics permit, regression validation, and durable progress or
blocker documentation. Preserve completed work and move past a documented
problem-specific blocker rather than stalling the corpus.

## Authorities to read before continuing

Use the current worktree as the source of truth, then read these files in full:

1. `AGENTS.md`
2. `BENCHMARKING.md`
3. `LEETCODE_SUBMISSIONS.md`
4. `dsa/leetcode/_template.md`
5. `dsa/leetcode/_reports/two_sum_migration_progress.md`
6. The next package's `metadata.json` and all existing artifacts

Do not infer current completion from this handoff alone. Refresh the audit
before selecting work.

## Reviewed documentation convention

- Use `Goal`, `Function Contract`, `Examples`, and `Required Complexity` in
  that order.
- Make `Goal` an original, source-faithful narrative with depth and length
  proportionate to the public statement. Follow the source problem's logical
  order as closely as independent wording permits: introduce the same scenario
  or data model, state every operation rule and guarantee that affects
  interpretation, preserve distinctions and boundary semantics, and finish
  with the exact requested outcome. Rephrase all prose rather than copying;
  fidelity means complete semantic coverage rather than sentence-level
  imitation or generic padding. Preserve source-native technical vocabulary
  exactly: never replace `ascending`, `non-decreasing`, `strictly increasing`,
  `subarray`, `subsequence`, `at most`, `exactly`, or another mathematical term
  with a near-synonym. Rephrase surrounding sentences, not relations or named
  concepts. Do not rewrite merely to make prose different: each change must
  improve clarity, sequencing, semantic coverage, or explanation of a material
  boundary condition. Keep source wording and structure when already clearest.
  Do not reduce a rich problem to one sentence.
- `Required Complexity` is notation-only: `Time: O(...)` and `Space: O(...)`.
- Write mathematical expressions in LaTeX (`$...$` inline or `$$...$$` as a
  display). Keep executable calculations—assignments, indexing, slices,
  function calls, pointer changes, and language operators—along with strings,
  serialized values, and other literal data in code spans. Use ordinary
  symbols, not code-styled identifiers, in abstract mathematics. Define every problem-specific complexity symbol
  before its compact bound is shown. The exact Required Complexity form is
  `- **Time:** $O(...)$` followed by `- **Space:** $O(...)$`.
- Only `Approach` is collapsible.
- Inside Approach, use exactly these three real level-four headings in order:
  `General`, `Complexity detail`, and `Alternatives and edge cases`.
- `Complexity detail` and `Alternatives and edge cases` are always required.
- Organize a substantial `General` section with tailored bold subheadings such
  as `**Why the unique pair must be found**`. These are bold paragraphs, not
  additional Markdown headings. Select them for the actual algorithm: name the
  greedy choice, state transition, critical invariant, trace, exchange
  argument, reconstruction step, or other idea that genuinely needs a signpost.
- Do not impose one repeated list of bold subheadings. A simple explanation may
  need fewer; a difficult one may need many and should be correspondingly long.
- Do not create generic repeated `Correctness` slots, numbered mini-templates,
  or mechanically copy Two Sum's paragraph sequence. Integrate correctness
  reasoning where it explains the relevant algorithmic idea.
- Write `Alternatives and edge cases` entirely as a scannable bullet list.
  Name each actual alternative in bold with a colon, such as
  `- **Visited matrix plus direction changes:** ...`, and explain its tradeoff
  or failure mode. Put each material boundary condition or semantic trap in a
  separate ordinary bullet. Do not replace this section with free-text
  paragraphs or force the same number of bullets for every problem.
- Do not add `Solution` or `Reference Implementations` sections to `doc.md`.
  Implementations belong in `solutions/`.

The durable version of these rules is recorded in `AGENTS.md` and
`dsa/leetcode/_template.md`.

## Current documentation priority

The source-fidelity review of every `Goal` from frontend ID 1 through 813 is
complete. The active follow-up is a mathematical-notation review of every
document from frontend ID 1 through 822. Problem 820 now defines
$S = \sum_{w \in \texttt{words}} \lvert w \rvert$ before using the compact
$O(S)$ time and space bounds. The corpus-wide pass has converted Required
Complexity bounds and mathematical prose to LaTeX; it must still complete its
semantic review, renderer validation, documentation tests, and dataset audit
before package migration resumes at problem 823.

## Per-package completion standard

For each package in numeric order:

1. Author the problem-specific document to the convention above.
2. Author visible samples, trials, and genuinely hidden correctness cases.
3. If multiple outputs are valid, use or add a semantic validator; never reject
   a valid user answer because it differs from one reference serialization.
4. Author exactly three increasing benchmark tiers with one consistent size
   meaning and at least a fourfold total span.
5. Calibrate the benchmarks: the reference and another implementation in the
   required class should pass; the principal correct slower class should pass
   outputs but fail scaling when the legal domain permits a meaningful test.
6. Preserve an app-local `solve(...)` reference and add a separate exact
   LeetCode-native declaration such as `class Solution`.
7. Submit the exact native artifact through the encrypted Electron credential
   bridge. Mark `submission.json` verified only after a remote Accepted result.
8. Run the package audit, dataset checker, focused tests, and `git diff --check`.
9. Record any genuine access or execution blocker and continue to the next ID.

## Current verified frontier

- Latest audit counts: 3985 packages, 819 locally complete, 819 fully complete
  and remotely verified, and 3 documented blockers.
- Problems through frontend ID 822 have authored documentation; the full
  verified count is 819 because the three blockers are tracked separately.
- Problem 820 was remotely Accepted as submission `2066596479`, problem 821 as
  `2066598728`, and problem 822 as `2066603979`.
- The next actionable package is
  `dsa/leetcode/823_binary-trees-with-factors` after the 1-through-822
  mathematical-notation review and its regression gates complete.

## Restart sequence

```powershell
git status --short
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py
Get-Content dsa\leetcode\_reports\two_sum_migration_progress.md
```

Then complete problem 823, calibrate it, remotely verify it if the connected
account has access, run the required checks, and continue in numeric order.

Useful validation commands:

```powershell
.\.venv\Scripts\python.exe tools\check_leetcode_dataset.py
.\.venv\Scripts\python.exe -m pytest server\tests\test_validated_cases.py server\tests\test_dynamic_docs.py -q
git diff --check -- <changed paths>
```

Maintainer submission command:

```powershell
$env:ELECTRON_RUN_AS_NODE=$null
npx.cmd --prefix electron electron electron/scripts/verify-leetcode-candidate.cjs lc_823
```

## Prompt for a new Codex session

> Resume the active canonical LeetCode migration in `C:\dawei7\code_n` with
> the same full goal through problem 3985. Read `AGENTS.md`, `BENCHMARKING.md`,
> `LEETCODE_SUBMISSIONS.md`, `dsa/leetcode/_template.md`, and
> `dsa/leetcode/_reports/ACTIVE_MIGRATION_HANDOFF.md` in full. Treat the live
> worktree and refreshed migration audit as authoritative, preserve all existing
> changes, and continue from the first actionable incomplete package in numeric
> order. Do not stop at a plan: implement, calibrate, remotely verify where
> permitted, run regression checks, document blockers, and continue. In each
> Approach, keep exactly `General`, `Complexity detail`, and `Alternatives and
> edge cases` as real headings; organize substantial General explanations with
> problem-specific bold subheadings like `**Why the unique pair must be found**`,
> never a repeated prose template. Keep `Alternatives and edge cases` as a
> bullet list: bold-name each alternative and use separate bullets for concrete
> edge cases; never drift back to free-text paragraphs.
