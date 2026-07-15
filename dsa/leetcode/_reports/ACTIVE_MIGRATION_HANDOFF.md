# Active LeetCode Migration Handoff

Updated: 2026-07-13

This work is active. It is neither complete nor globally blocked. The full
goal remains the canonical migration of every problem through frontend ID
3985. This handoff records the current live boundary for a new Codex session;
the worktree and freshly generated reports remain authoritative if anything
below has drifted.

## Full goal

Migrate every canonical LeetCode package in `C:\dawei7\code_n`, in ascending
numeric frontend-ID order through problem 3985, to the reviewed Two Sum
standard. A completed package needs:

1. an original, source-faithful `doc.md`;
2. visible samples, trials, and meaningful hidden correctness cases;
3. exactly three ordered, complexity-sensitive benchmark tiers;
4. an optimal app-local solution for every runnable supported environment;
5. a separate exact LeetCode-native submission artifact;
6. remote Accepted verification where account access and execution semantics
   permit it;
7. regression checks; and
8. durable progress or blocker documentation.

Preserve all existing changes. If one problem is genuinely blocked, document
the problem-specific reason and continue to the next numeric frontend ID.

## Repository and branch state

- Repository: `C:\dawei7\code_n`
- Current local branch: `agent/leetcode-migration-823`
- Current base commit: `1fc55b6e7ff0e808e207376bc663ea60cb2cb798`
- The current branch has no remote branch and contains uncommitted problem 823
  artifacts plus refreshed generated reports and this handoff.
- Commit `1fc55b6e` is also the tip of
  `origin/agent/zero-pad-leetcode-packages`.
- Draft PR #1 contains only the directory-padding migration:
  <https://github.com/dawei7/code_n/pull/1>
- `main` and `origin/main` are still at `3f0040f9`. They do not yet contain the
  zero-padded package paths. Do not switch to `main` and then recreate or move
  the current work.
- Do not commit, push, merge the draft PR, or publish a release without a new
  explicit user request. The earlier commit/push authorization applied to the
  directory-padding change, not automatically to subsequent migration work.

Canonical problem directories now use four-digit frontend-ID prefixes, for
example `dsa/leetcode/0001_two-sum` and
`dsa/leetcode/0824_goat-latin`. All 3985 canonical package directories were
renamed and the padding migration was hash-verified. Lexicographic directory
order now equals numeric frontend-ID order. Personal user-data paths are a
separate compatibility surface and intentionally remain unpadded, for example
`dsa/leetcode/1_two-sum/user_solutions/...` under the user-data root.

## Authorities to read completely before acting

Read these files in full, in this order:

1. `AGENTS.md`
2. `BENCHMARKING.md`
3. `LEETCODE_SUBMISSIONS.md`
4. `dsa/leetcode/_template.md`
5. `dsa/leetcode/_reports/ACTIVE_MIGRATION_HANDOFF.md`
6. `dsa/leetcode/_reports/two_sum_migration_progress.md`

Then refresh the migration audit and inspect the next package's
`metadata.json` and every existing artifact. Do not infer the current frontier
from chat history or this file alone.

## Problem-statement writing convention

- Use `Goal`, `Function Contract`, `Examples`, and `Required Complexity`, in
  that order.
- The Goal must be original prose, not a copied LeetCode statement. It should
  nevertheless stay close to the public problem's intent, logical order,
  technical vocabulary, semantic coverage, and proportionate length. A long
  or nuanced source problem should not collapse into a generic short summary.
- Rephrase to improve clarity, sequencing, or completeness, not merely to make
  the words different. Preserve already-clear mathematical and technical
  terms. In particular, never replace `ascending` with `non-decreasing`, or
  interchange `strictly increasing`, `subarray`, `subsequence`, `at most`,
  `exactly`, or similar terms merely as stylistic variation.
- State every operation rule, guarantee, boundary condition, output condition,
  and distinction that changes how the problem is solved.
- Use only public problem facts needed to author an independent summary. Do
  not copy full LeetCode statements, examples, editorials, or proprietary
  solution prose. The metadata table owns the only official external problem
  link and labels it `LeetCode`.
- Do not add `Solution` or `Reference Implementations` sections to `doc.md`.
  Implementations belong under `solutions/`.

## Mathematical notation versus executable code

This distinction is a durable requirement for all reviewed documents, not a
problem-820-only cleanup.

- Write abstract mathematics in LaTeX: `$n$`, `$x = yz$`,
  `$1 \le n \le 1000$`, `$10^9 + 7$`, `$O(n^2)$`, and sums or recurrences.
- Prefer a display definition when a long expression would make a rendered
  line unreadable. Define a short symbol once and use it in the bounds. For
  example:

  $$
  S = \sum_{w \in \texttt{words}} \lvert w \rvert.
  $$

  Then write the relevant bound as `$O(S)$`, not the full summation twice.
- Define every problem-specific complexity symbol before using it. Standard
  input-size symbols such as `$n$` must still be tied to the concrete input,
  for example "Let `$n$` be the length of `arr`."
- Keep executable calculations and language syntax in code spans rather than
  converting them to LaTeX. This includes assignments, indexing, slices,
  function calls, pointer changes, and programming-language operators. Correct
  examples are `nums[a] = target - nums[b]`, `ways[root] += ...`, `arr[i:j]`,
  `left += 1`, and `solve(arr)`.
- Strings, serialized values, identifiers used as literal program objects, and
  input/output fragments also remain code. Use `\texttt{...}` inside LaTeX
  only when the identifier genuinely participates in an abstract mathematical
  definition, as `words` does in the displayed definition of `$S$` above.
- `Required Complexity` is notation-only and has exactly this form, with no
  explanatory prose in that section:

  ```markdown
  - **Time:** $O(...)$
  - **Space:** $O(...)$
  ```

The corpus-wide mathematical-notation review through problem 822 is complete.
Problem 820 now defines the total input-character count with the displayed
symbol `$S$` before using `$O(S)$`. The documentation tests, dataset checker,
full Python regression suite, Ruff, web build, Electron build, and diff checks
for that pass and the directory-padding migration were completed successfully
before problem 823 began.

## Approach-section convention

- Only `Approach` is collapsible.
- Inside Approach, use exactly these three level-four headings, in this order:
  `General`, `Complexity detail`, and `Alternatives and edge cases`.
- Do not add any other Markdown headings inside Approach.
- Use optional, problem-specific bold signposts inside `General` when they
  improve navigation, such as `**Why the unique pair must be found**`. They are
  bold paragraphs, not headings and not a repeated mini-template.
- Derive the algorithm from the problem's constraints and integrate the reason
  it is correct with the idea being explained. Do not insert generic repeated
  `Correctness`, invariant, trace, proof, or fixed-count slots when they do not
  improve that particular explanation.
- Match depth to difficulty. Simple observations may be concise; complex
  algorithms need the state definitions, transitions, examples, and reasoning
  necessary to teach them accurately.
- Write `Alternatives and edge cases` entirely as a bullet list. Bold-name each
  genuine alternative and state its tradeoff or failure mode, for example
  `- **Visited matrix plus direction changes:** ...`. Give each material edge
  case or semantic trap a separate bullet. Do not use free-text paragraphs or
  force a fixed number of bullets.

## Identity and submission rules

- Preserve the numeric frontend ID, title slug, official URL, language,
  category, and source-native execution semantics.
- LeetCode's backend `question_id` is not the frontend ID and may legitimately
  differ. For example, frontend problem 497 has internal question ID 914.
  Record both values from the authoritative metadata; never overwrite the
  internal ID merely because the frontend ID looks more familiar.
- Keep the app-local `solve(...)` implementation and the native artifact side
  by side. The native file must retain the platform declaration and exact
  method signature, such as `class Solution`.
- A candidate remains unverified until the exact native source is remotely
  Accepted. Local correctness alone never promotes `submission.json`.
- The user has already authorized in-scope remote verification submissions for
  this continuing migration through the existing Electron credential bridge.
  Do not ask for a separate confirmation for every problem when the execution
  environment permits the direct command. Do not add approval-escalation
  flags. If the host UI itself enforces a confirmation, that policy cannot be
  bypassed from repository code.
- If work is paused only by the transient message "Selected model is at
  capacity", retry after about five minutes and continue from the live audit.

## Per-package completion loop

For each package in ascending numeric frontend-ID order:

1. Confirm public identity and contract facts from the official LeetCode page
   or public GraphQL metadata when needed, then write an independent document.
2. Author visible samples, trials, and meaningful hidden correctness cases.
3. If multiple outputs are valid, use or add a semantic validator; never reject
   a valid output solely because its serialization differs.
4. Author exactly three increasing benchmark tiers with one consistent `size`
   meaning, unique positive sizes, and at least a fourfold total span.
5. Calibrate the benchmark. The reference and a separate implementation in the
   required complexity class must pass. A correct principal slower-class
   implementation must return every expected output and fail only the
   complexity verdict whenever the legal domain permits such a distinction.
   A safety-cap failure is not an acceptable substitute for scaling evidence.
6. Preserve the app-local solution and add the native LeetCode artifact.
7. Submit that exact native artifact and promote the manifest only on remote
   Accepted evidence.
8. Refresh the audit and dataset report, run focused regression tests, and run
   `git diff --check`.
9. Record a genuine blocker with exact evidence and continue numerically.

## Current verified frontier

Problem 823, Binary Trees With Factors, is complete on the current uncommitted
branch:

- Package: `dsa/leetcode/0823_binary-trees-with-factors`
- LeetCode frontend ID: 823
- LeetCode internal question ID: 843
- Native entrypoint: `Solution.numFactoredBinaryTrees`
- App-local and native algorithms: sorted dynamic programming with a value-to-
  count map; `$O(n^2)$` time and `$O(n)$` auxiliary space.
- Correctness suite: 12 ordinary cases plus 3 benchmark cases, 15 total.
- Benchmark sizes: 32, 128, and 512 unique values, a 16-fold span. Each is a
  prefix of the sorted nonunit divisors of 73513440 so the tiers contain a
  dense lattice of valid factor dependencies.
- The canonical implementation and an independently structured quadratic
  factor-pair implementation passed every case and the scaling verdict.
- For calibration, the correct slower implementation linearly materialized
  prior pair products with `list(map(left.__mul__, previous))`. It returned all
  15 expected outputs and failed only scaling: relative extra growth `+0.53`
  exceeded `0.15`, and its largest reference ratio was `9.32x`.
- Exact native source remotely Accepted as LeetCode submission `2066667507`.
  `submission.json` was promoted to `verified` by the verifier.

Fresh audit after that acceptance:

- 3985 canonical packages
- 820 locally complete
- 820 fully complete and remotely verified
- 3 documented fixed-domain benchmark blockers
- 823 documents complete under the migration audit
- 1484 correctness-case packages complete
- 820 benchmark packages complete
- 1679 optimal app-local solutions complete
- 823 native submissions complete
- First actionable incomplete package: frontend ID 824, Goat Latin, at
  `dsa/leetcode/0824_goat-latin`

The separate dataset completion report currently records 2192 documents as
manually complete and 1793 as needing authoring. It is a broader documentation
inventory, not permission to skip the audit's first actionable package.

Known benchmark blockers remain frontend IDs 401, 405, and 479. Their exact
fixed-domain reasons and accepted submission evidence are recorded in
`dsa/leetcode/_reports/two_sum_migration_progress.md`.

## Verification evidence at this boundary

The following checks passed after problem 823 was authored and remotely
verified:

- `tools/audit_leetcode_migration.py`
- `tools/check_leetcode_dataset.py`
- `server/tests/test_validated_cases.py` and
  `server/tests/test_dynamic_docs.py`: 89 passed, with only the existing
  Starlette `httpx` deprecation warning
- `git diff --check` before the final handoff rewrite; run it once more at the
  start of the next session because this handoff itself was then changed

The preceding mathematical-notation and zero-padding batch also passed the
full Python suite (266 tests and 23910 generated subtests), Ruff, the web build,
the Electron build, the dataset checker, the migration audit, and diff checks.

## Exact restart sequence

Start in the existing checkout and keep its uncommitted changes:

```powershell
Set-Location C:\dawei7\code_n
git branch --show-current
git status --short --branch
git rev-parse HEAD
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py
Get-Content dsa\leetcode\_reports\two_sum_migration_progress.md
```

The expected branch is `agent/leetcode-migration-823`, the expected base commit
is `1fc55b6e7ff0e808e207376bc663ea60cb2cb798`, and the refreshed first
actionable package should be `dsa/leetcode/0824_goat-latin`. If any of those
facts differ, trust the live worktree and refreshed audit, investigate the
drift, and preserve rather than discard changes.

After completing each package, use at least:

```powershell
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py
.\.venv\Scripts\python.exe tools\check_leetcode_dataset.py
.\.venv\Scripts\python.exe -m pytest server\tests\test_validated_cases.py server\tests\test_dynamic_docs.py -q
git diff --check
```

For the next native candidate, replace the frontend ID in:

```powershell
$env:ELECTRON_RUN_AS_NODE=$null
npx.cmd --prefix electron electron electron/scripts/verify-leetcode-candidate.cjs lc_824
```

## Exact prompt for a new Codex session

Copy and paste this entire block into the new session:

> Resume the active canonical LeetCode migration in `C:\dawei7\code_n` with
> the full goal of completing every problem through frontend ID 3985. Stay on
> the existing local branch `agent/leetcode-migration-823`, which is based on
> zero-padding commit `1fc55b6e7ff0e808e207376bc663ea60cb2cb798`, and preserve
> every uncommitted change. Do not switch to `main`: draft PR #1 contains the
> four-digit canonical directory migration and has not been merged. Before
> changing anything, read `AGENTS.md`, `BENCHMARKING.md`,
> `LEETCODE_SUBMISSIONS.md`, `dsa/leetcode/_template.md`,
> `dsa/leetcode/_reports/ACTIVE_MIGRATION_HANDOFF.md`, and
> `dsa/leetcode/_reports/two_sum_migration_progress.md` completely. Then run a
> fresh migration audit and treat the live worktree and generated reports as
> authoritative. Problem 823 is locally complete and remotely Accepted as
> submission `2066667507`; the expected first actionable package is
> `dsa/leetcode/0824_goat-latin`, but follow the refreshed audit if it differs.
> Continue autonomously in numeric frontend-ID order and do not stop after
> planning. For every problem, finish the source-faithful original
> documentation, correctness cases, exactly three complexity-sensitive
> benchmark tiers, optimal app-local solution, separate native LeetCode
> artifact, remote Accepted verification where permitted, regression checks,
> and progress or blocker documentation. Keep canonical package directory
> prefixes four digits, while leaving personal user-data paths unpadded. In
> `Goal`, preserve the source's technical vocabulary, logical order, semantic
> detail, and proportionate length; rephrase only to improve clarity or remain
> independently written, never for variation alone and never by changing terms
> such as `ascending` into `non-decreasing`. Use LaTeX for abstract mathematics
> and complexity, define long expressions with a short mathematical symbol,
> and keep executable assignments, indexing, function calls, slices, pointer
> changes, operators, strings, and serialized values in code spans rather than
> LaTeX. `Required Complexity` must contain only `- **Time:** $O(...)$` and
> `- **Space:** $O(...)$`, with any problem-specific symbols defined earlier.
> Inside Approach, use only `General`, `Complexity detail`, and `Alternatives
> and edge cases` as real headings. Use problem-specific bold signposts inside
> substantial General explanations without creating another repeated prose
> template. Keep `Alternatives and edge cases` entirely as bullets: bold-name
> each alternative and give separate bullets for material edge cases. Preserve
> LeetCode frontend IDs separately from backend `question_id` values. Use the
> existing Electron credential bridge for the in-scope remote submissions
> already authorized by the user without asking for per-problem confirmation
> when the environment permits it. A correct slower-class benchmark candidate
> must return all expected outputs and fail the scaling verdict, not a safety
> cap. If a problem is genuinely blocked, record exact evidence and move on.
> Do not commit, push, merge, or release unless the user explicitly authorizes
> that new external change. If model capacity temporarily pauses the session,
> retry after about five minutes and continue from the refreshed audit.
