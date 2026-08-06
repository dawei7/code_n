# Solution Quality and Deferred Case Quality

This workflow manually reviews each canonical LeetCode package after its normal
completion gates. The active accelerated campaign asks whether the app-local
Optimal solution is clear, concise, conventional, and suitable for an expert
interview while completing its source-faithful modular Reference. Correctness-
case and benchmark-calibration review remain defined here for a separate future
campaign.

The review is independent of source fidelity, remote submission evidence, and
app/native structural alignment. Identical app and native implementations can
still be poor interview code.

## Current campaign scope

The active 4,005-package expert-quality campaign completes Premium packages
first and exclusively. Process one Premium package at a time. Use ascending
frontend-ID order for the expanded Premium queue, except that an already-started
package must be finished before returning to the queue head.

A Premium package is complete for this campaign only when all four conditions
are current:

1. The Optimal solution has a current, hash-bound solution-quality review.
   New accelerated reviews use `review_scope` equal to `solution_only`; an
   earlier current `solution_and_cases` review still satisfies this solution
   condition independently of case status.
2. The complete `variants/optimal/approach.md` has been reviewed against that
   solution or its inert candidate.
3. The package uses the modular `reference/` structure.
4. Its `source_fidelity.json` validates as `verified` against authoritative live
   source evidence.

Derive the queue from solution-quality completion plus verified source fidelity
and ignore case-quality status. A campaign review sets `review_scope` to
`solution_only`, omits `case_review`, and hash-binds the reviewed solution,
immutable native source, selected approach, variant manifest, inherited
complexity artifact, and candidate when one exists. A benchmark hash records
artifact identity only; it does not claim a fresh calibration review.

Run direct package validators and protected-file integrity checks after every
completed package. After every fifty campaign completions, and once more before
session handoff, regenerate the complete dataset report without
`--solution-only`, run the migration audit, reopen the refreshed reports, and
rederive the Premium queue:

```powershell
.\.venv\Scripts\python.exe tools\check_leetcode_dataset.py
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py
```

## Review boundary

- Review packages individually in ascending frontend-ID order.
- Do not infer approval from formatting, alignment, local correctness, or a
  remotely Accepted native submission.
- Do not edit `solve.py`, another active app-local solution, `leetcode.*`, or
  `submission.json` during a proposal-only review.
- When a material improvement is warranted, add exactly one inert
  `variants/optimal/solutions/candidate.<extension>` using the app-local
  function contract. The application and variant loader must continue to
  ignore that file.
- When no material improvement is warranted, do not leave a candidate file.
- Keep every candidate inert. Never promote or submit it, and never represent it
  as remotely Accepted.
- Preserve metadata and `solution_variants.json` unless a separately proven
  defect requires an authorized change.
- Do not proactively inspect, expand, rewrite, reclassify, calibrate, or review
  `cases.json` or `benchmark.json`. Do not create `case_review` evidence, add
  replacement correctness cases, or claim case-quality completion. Keep
  `benchmark.json` byte-for-byte unchanged.
- When no candidate is created, do not run or analyze the package's cases or
  benchmarks. When a material candidate is created, run the existing unchanged
  judge only as a black-box compatibility gate.
- If a candidate fails an ordinary case, inspect only that failing case. Delete
  it only when authoritative source evidence independently proves the case is
  wrong and the candidate is correct; never delete a case merely to make a
  candidate pass, and never replace a deleted case.
- If a candidate fails benchmark evidence, do not inspect or modify the
  benchmark. Do not record the candidate as approved; preserve the protected
  solution and report it as inconclusive or omit it.

## Solution-quality standard

A completed review confirms all of the following:

1. The target implementation obeys the source contract by expert review. A
   newly created candidate must also pass the existing unchanged judge as a
   black-box compatibility gate; the protected solution is not rerun merely to
   complete this campaign review.
2. Its asymptotic time and space meet the Optimal branch requirements.
   Confirm this from the algorithm and inherited complexity evidence without
   recalibrating or analyzing the benchmark. Micro-optimizations are irrelevant
   unless they materially affect the required complexity or obscure the code.
3. The algorithm is direct and recognizable. Avoid code golf, packed values,
   obscure library tricks, unnecessary abstractions, and mutable state that a
   simpler formulation does not need.
4. Names follow conventional mathematical and interview notation. Use `i`,
   `j`, `k`, `x`, `y`, `u`, `v`, `r`, and `c` where those meanings are clear.
   Never use a local variable named `index`; use descriptive names only for
   genuine algorithmic concepts such as `left`, `right`, `parent`, `indegree`,
   `distance`, or `prefix_length`.
5. Control flow is easy to explain, nesting is justified, and edge conditions
   are visible where they matter.
6. Formatting follows the repository formatter: four-space indentation and a
   120-column line length, with readable long lines preferred over unstable or
   gratuitous wrapping.
7. `approach.md` describes the review target's exact algorithm, data flow, and
   complexity. A candidate-targeted approach is explicitly recorded as such;
   it is never represented as matching the unchanged active solution.

## Deferred correctness-case standard

The following standard is preserved for a separate future case-quality and
benchmark-calibration campaign. It is not a completion condition and must not
be applied proactively during the active accelerated campaign.

Correctness cases and performance workloads have different purposes:

- `cases.json` contains only user-visible `sample` and `trial` cases. Every row
  explicitly uses `"visible": true`.
- `benchmark.json` contains only hidden `benchmark` cases. Performance inputs
  are not presented as correctness examples.
- The correctness suite covers every source example, contract boundary,
  materially different control-flow exit, input-shape distinction, and
  semantic trap relevant to the problem. The number of cases follows the
  problem; no fixed quota substitutes for manual sufficiency review.
- Expected values and specialized validators are reviewed against the contract.
- Benchmarks still exercise the complexity-sensitive path with legal inputs,
  ordered scaling tiers, and the required complexity verdict.

## Durable evidence

Each accelerated review is recorded in
`variants/optimal/solution_quality.json` with `review_scope` equal to
`solution_only`. It records the solution review, omits `case_review`, identifies
`current` or `candidate` as the solution and approach target, and hash-binds the
reviewed solution, immutable native source, complete approach, variant
manifest, inherited complexity artifact, and candidate when present. A changed
bound artifact makes the review stale.

The generated `dsa/leetcode/_reports/_completion_report.json` aggregates:

- `solution_quality_status` and the separately deferred `case_quality_status`
  per package;
- the current/candidate verdict and candidate path;
- counts for every status and verdict; and
- the first incomplete package for each review dimension.

A missing manifest means `unreviewed`, never implicitly good. The active queue
uses `solution_quality_status` plus verified source fidelity and ignores
`case_quality_status`. A completed candidate proposal means the proposed target
is good; it does not authorize promotion into the active or native solution.
