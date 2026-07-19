# Runtime and Complexity Benchmarking

This document defines the benchmark standard for cOde(n). The canonical,
reviewed example is the Two Sum package:

- `dsa/leetcode/0001_two-sum/cases.json`
- `dsa/leetcode/0001_two-sum/benchmark.json`
- `dsa/leetcode/0001_two-sum/variants/optimal/solutions/python.py`
- `dsa/leetcode/0001_two-sum/doc.md`

Future corpus migrations should reproduce the behavior described here, adapted
to each problem's actual inputs and required complexity.

## Verdict model

A successful submission must satisfy two independent requirements:

1. **Correctness:** every authored official case returns an accepted result.
2. **Complexity:** either the user/reference runtime ratio remains sufficiently
   stable as the authored workload size increases, or the package has a
   strictly validated non-scaling certificate for a contract where runtime
   scaling is genuinely inapplicable.

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

Every package owns exactly one legal benchmark at the problem root. The
Optimal branch is the timing reference, while every published Simplified
branch must pass that unchanged benchmark and its correctness checks. Never
add oversized, out-of-contract, or specially relaxed tiers merely to make a
simplified implementation pass; LeetCode's real input limits are part of the
shared problem contract.

A one-case sidecar remains supported for packages that have not been migrated.
It uses the legacy rule `user runtime <= 1.5 * reference runtime`.

## Non-scaling complexity certificates

Scaling is the default and preferred verification method. Do not create a
certificate merely because calibration is inconvenient. A package may use
`complexity_certificate.json` instead of `benchmark.json` only in one of these
reviewed situations:

- `bounded_domain`: the complete legal source domain imposes a fixed maximum
  workload too small to support a stable scaling trend;
- `bounded_concurrency`: the contract has a fixed or tightly bounded number of
  concurrent operations, so safety, callback order, progress, and deadlock
  evidence are the meaningful verification targets; or
- `asymptotic_optimality`: a problem-level lower bound matches the required
  upper bound and no genuine principal slower algorithmic class exists within
  the source semantics.

The certificate is a separate artifact so reports never claim that a runtime
benchmark exists when it does not:

```json
{
  "schema_version": 1,
  "challenge_id": "lc_401",
  "status": "verified",
  "method": "bounded_domain",
  "required_time": "O(1)",
  "summary": "The complete legal input domain has a fixed workload bound.",
  "workload_bound": {
    "symbol": "B",
    "maximum": 1024,
    "unit": "LED masks",
    "source_constraint": "turned_on is an integer from 0 through 10"
  },
  "replacement_checks": [
    {
      "kind": "bounded_work_proof",
      "evidence": "Four hour LEDs and six minute LEDs produce 2^10 masks."
    },
    {
      "kind": "exhaustive_domain",
      "evidence": "Regression tests evaluate every legal input value."
    }
  ]
}
```

`engine/complexity_certificates.py` owns the strict schema. It rejects generic
waivers, missing workload bounds, incomplete optimality arguments, duplicate or
unsupported evidence kinds, mismatched challenge IDs, and unverified status.
A completed scaling benchmark and a completed certificate must not coexist.

Replacement evidence is method-specific:

- bounded domains require a bounded-work proof plus exhaustive-domain or
  boundary/property verification;
- asymptotic optimality requires explicit lower-bound and upper-bound proofs
  plus boundary/property verification; and
- bounded concurrency requires a bounded-work proof, scheduler stress,
  semantic validation, and a deadlock timeout.

Certificates verify the source contract's complexity-verification method. They
do not weaken correctness, source fidelity, remote submission verification, or
the execution safety cap. Real-test responses and the Complexity panel must
label the certificate method directly; `runtime_check` remains false because
no runtime scaling verdict was measured.

## Measurement method

Each tier compares the user solution with the same-language optimal reference
from the package's `variants/optimal/solutions/` directory.

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
- A certified non-scaling package shows the verified certificate method and
  evidence summary, labels runtime tiers as not applicable, and never displays
  certificate evidence as a benchmark measurement.

## Corpus migration checklist

For each LeetCode package:

1. Confirm the required time complexity in metadata and `doc.md`.
2. Confirm the package has a correct same-language optimal reference.
3. Keep ordinary samples, trials, and hidden correctness cases in `cases.json`.
4. Author three representative, increasing benchmark tiers in
   `benchmark.json` with a consistent `size` definition and at least a `4x`
   total span. Only when the contract meets one of the reviewed non-scaling
   conditions, author and validate `complexity_certificate.json` instead.
5. For a benchmark, make the tiers distinguish the required class from the
   most plausible slower alternative without making constant-factor style
   differences decisive. For a certificate, implement every method-specific
   replacement check and reject a generic waiver.
6. Verify the optimal reference passes.
7. For a benchmark, verify at least one different implementation in the
   required class passes.
8. For a benchmark, verify a correct implementation from the principal slower
   class passes all outputs but fails scaling.
9. Verify malformed, non-terminating, and incorrect solutions still fail for
   the appropriate reason.
10. Inspect the result UI and ensure no hidden evidence is exposed and the
    verification method is labeled accurately.

Do not mass-copy Two Sum's numeric sizes. Benchmark sizes and inputs must be
authored for each problem's semantics and runtime characteristics.

## Resolved-blocker recovery reference

The historical eighteen-problem blocker set has a reviewed per-ID recovery
guide at `dsa/leetcode/_reports/ORIGINAL_18_BLOCKER_PLAYBOOK.md`. Read it when
one of those entries regresses or when restoring the source-native concurrency
runtime. It records which five problems require scaling, which thirteen require
certificates, the accepted workload variables and tiers, semantic validators,
and the evidence required before clearing a blocker. The general rules in this
document still take precedence if the corpus later evolves.

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
