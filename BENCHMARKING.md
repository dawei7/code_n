# Runtime and Complexity Benchmarking

This document defines the benchmark standard for cOde(n). The canonical,
reviewed example is the Two Sum package:

- `dsa/leetcode/1_two-sum/cases.json`
- `dsa/leetcode/1_two-sum/benchmark.json`
- `dsa/leetcode/1_two-sum/solutions/python.py`
- `dsa/leetcode/1_two-sum/doc.md`

Future corpus migrations should reproduce the behavior described here, adapted
to each problem's actual inputs and required complexity.

## Verdict model

A successful submission must satisfy two independent requirements:

1. **Correctness:** every authored official case returns an accepted result.
2. **Complexity:** the user/reference runtime ratio remains sufficiently stable
   as the authored workload size increases.

A terminating implementation from a slower complexity class is still a correct
implementation. It must pass the case list and then fail the complexity panel.
For example, the conventional nested-loop Two Sum solution is functionally
correct but `O(n^2)`, so all of its case indicators are green while its scaling
verdict fails. Do not present that outcome as an incorrect hidden answer.

The Python step limit is an execution safety mechanism, not the complexity
judge. Benchmark correctness runs therefore receive a larger safety allowance
than ordinary cases so that realistic slower implementations reach the scaling
verdict. Truly runaway code may still be stopped by the safety cap.

## Benchmark sidecar contract

Runtime inputs live in `benchmark.json`, separate from the user-facing
`cases.json`. A scaling benchmark requires at least two tiers; three tiers are
recommended because they establish a trend instead of relying on one endpoint
comparison.

```json
{
  "challenge_id": "lc_1",
  "cases": [
    {
      "id": "benchmark-scale-1",
      "name": "benchmark: late pair at n=32",
      "kind": "benchmark",
      "visible": false,
      "size": 32,
      "input": {"nums": [], "target": 0},
      "expected": [30, 31],
      "tags": ["benchmark", "scale-small"]
    }
  ]
}
```

For a multi-tier sidecar:

- Every `kind` must be `benchmark`.
- Every `size` must be a positive integer.
- Sizes must be unique and stored in increasing order.
- The largest size must be at least four times the smallest.
- Every tier must test the same algorithmic behavior and use the same meaning
  for `size`.
- Inputs should exercise the complexity-sensitive path. Two Sum places the
  valid pair at the end so a quadratic scan cannot exit early.
- Expected results and validators must remain semantically correct; benchmark
  inputs are not exempt from correctness checking.

`size` is the authored workload variable used for the scaling regression. Use
the parameter that governs the required complexity: list length for a one-list
problem, total cells for an area-based grid algorithm, or another documented
monotonic measure when the input has multiple dimensions.

A one-case sidecar remains supported for packages that have not been migrated.
It uses the legacy rule `user runtime <= 1.5 * reference runtime`.

## Measurement method

Each tier compares the user solution with the same-language optimal reference
from the package's `solutions/` directory.

The timing procedure:

1. Runs one pilot for the reference and one for the user.
2. Selects one shared amplification factor, normalized out of displayed times.
3. Runs at least seven paired trials, alternating which implementation runs
   first to reduce cache, garbage-collection, and CPU-frequency bias.
4. Uses the median of paired user/reference ratios.
5. Fits a linear regression to `log(runtime ratio)` versus `log(size)` across
   tiers.

The fitted slope is the user's **extra growth exponent** relative to the
reference. Constant implementation overhead keeps the ratio approximately flat
and therefore contributes little to the slope.

The current scaling gate passes when both conditions hold:

- extra growth exponent is at most `0.15`;
- the largest-tier user/reference ratio is at most `8x`.

The `8x` rule is a safety cap for pathological constant overhead, not the main
complexity test. Timing is a robust heuristic rather than a mathematical proof;
there is deliberately no source-text, AST-shape, or bytecode-identity shortcut.

One submission starts one performance phase. The paired trials and any
amplified calls are internal samples within that phase, not repeated test
submissions.

## UI contract

- Correctness and complexity must be reported separately.
- Benchmark inputs remain hidden and must not reveal inputs or expected values.
- A correct but slower-complexity solution shows every case as correct and a
  failed complexity-scaling verdict.
- A multi-tier result shows size, user runtime in the app accent color, optimal
  reference runtime in green, per-tier ratio, and extra growth exponent.
- A single-tier legacy result shows the fixed runtime target instead.
- The optimal solution remains locked until the complete acceptance verdict is
  achieved.

## Corpus migration checklist

For each LeetCode package:

1. Confirm the required time complexity in metadata and `doc.md`.
2. Confirm the package has a correct same-language optimal reference.
3. Keep ordinary samples, trials, and hidden correctness cases in `cases.json`.
4. Author three representative, increasing benchmark tiers in
   `benchmark.json` with a consistent `size` definition and at least a `4x`
   total span.
5. Make the tiers distinguish the required class from the most plausible slower
   alternative without making constant-factor style differences decisive.
6. Verify the optimal reference passes.
7. Verify at least one different implementation in the required class passes.
8. Verify a correct implementation from the principal slower class passes all
   outputs but fails scaling.
9. Verify malformed, non-terminating, and incorrect solutions still fail for
   the appropriate reason.
10. Inspect the result UI and ensure no hidden evidence is exposed.

Do not mass-copy Two Sum's numeric sizes. Benchmark sizes and inputs must be
authored for each problem's semantics and runtime characteristics.

## Validation

Run focused benchmark tests while authoring, then the repository checks:

```powershell
.\.venv\Scripts\python.exe -m pytest server\tests\test_validated_cases.py -q
.\.venv\Scripts\python.exe tools\check_leetcode_dataset.py
.\.venv\Scripts\python.exe -m pytest -q
npm.cmd run build --prefix web
git diff --check
```

The Two Sum regression suite specifically verifies that its three sizes are
ordered and that the quadratic solution is reported as correct-but-too-slow,
not as a wrong hidden case.
