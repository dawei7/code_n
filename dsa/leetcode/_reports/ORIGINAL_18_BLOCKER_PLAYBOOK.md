# Original 18 Complexity Blockers: Resolution Playbook

This is a recovery guide for the eighteen complexity blockers that appeared
while the canonical migration advanced through frontend ID 1267. They are
resolved in the current worktree. Do not recreate their blocker records or
replace their reviewed artifacts merely because an old handoff mentions them.
If a fresh audit reports one again, use the live package and the procedure
below to find the regression.

This playbook supplements `AGENTS.md` and `BENCHMARKING.md`; those files remain
authoritative. It does not waive documentation, correctness, optimal-source,
native-artifact, remote-Accepted, or regression requirements.

## Resolution map

Five problems have a legal scalable workload and therefore use exactly three
runtime benchmark tiers:

| Frontend ID | Workload symbol and tiers | Required distinction |
| ---: | --- | --- |
| 1115 | handoffs $n$: 50, 200, 800 | constant work per `foo`/`bar` handoff versus rescanning a growing prefix |
| 1116 | terminal integer $n$: 50, 200, 800 | constant work per emitted value versus rescanning prior output |
| 1117 | molecule count $M$: 1, 5, 20 | three coordinated callbacks per molecule versus scanning prior molecule state per atom |
| 1195 | terminal integer $n$: 1, 10, 50 | one condition-variable transition per value versus rebuilding the emitted prefix |
| 1242 | reachable vertices $V$: 8, 32, 128 | hash-set discovery on a dense same-host graph versus linear-list duplicate detection |

The other thirteen do not have an honest source-valid scaling experiment.
They use a strict `complexity_certificate.json`, never an empty or fabricated
benchmark:

| Frontend ID | Certificate method | Why scaling is inapplicable |
| ---: | --- | --- |
| 401 | `bounded_domain` | `turned_on` has eleven legal values and the clock has only 1024 LED masks. |
| 405 | `bounded_domain` | A signed 32-bit integer yields at most eight hexadecimal digits. |
| 479 | `bounded_domain` | The legal input is only $1 \le n \le 8$ and the optimal result is an eight-value table. |
| 999 | `bounded_domain` | Every legal board is exactly $8 \times 8$. |
| 1108 | `bounded_domain` | A valid IPv4 address has fixed structure and at most fifteen characters. |
| 1114 | `bounded_concurrency` | Exactly three calls must satisfy one happens-before order; all six launch permutations are testable. |
| 1118 | `bounded_domain` | Each call selects one of twelve months and performs fixed leap-year arithmetic. |
| 1134 | `bounded_domain` | The largest legal input has nine decimal digits. |
| 1137 | `bounded_domain` | The source restricts $n$ to the range from 0 through 37. |
| 1154 | `bounded_domain` | The input is a fixed ten-character date and at most twelve month lengths are examined. |
| 1165 | `asymptotic_optimality` | Every word character must be inspected, giving $\Omega(m)$, and the reference achieves $O(m)$ over a fixed 26-key alphabet. |
| 1188 | `bounded_concurrency` | Capacity is at most 30 and the source permits at most 40 queue-method calls. |
| 1226 | `bounded_concurrency` | There are always five philosophers and at most 300 requests; safety and progress are the real properties. |

Do not move an ID between these groups without new source-contract evidence.
In particular, small or noisy timings are not permission to replace one of the
five scalable benchmarks with a certificate.

## Shared concurrency runtime prerequisite

Frontend IDs 1114, 1115, 1116, 1117, 1188, 1195, 1226, and 1242 must be
executable before their complexity evidence can count. If several of these
regress together, repair the shared runtime rather than editing eight packages
independently:

1. `engine/special_environments.py` must classify `concurrency` as runnable and
   as a special environment.
2. `challenges/algorithms/leetcode.py` must load the complete source-native
   Python class for concurrency references and starters. Do not replace
   `Foo`, `FooBar`, `ZeroEvenOdd`, `H2O`, `BoundedBlockingQueue`, `FizzBuzz`,
   `DiningPhilosophers`, or the crawler `Solution` with an app-only `solve(...)`
   signature.
3. `server/app/special_environments.py` must execute user source in an isolated
   Python subprocess, dispatch only the eight reviewed challenge IDs, capture
   callback results, join worker threads, and convert a timeout or live worker
   into an explicit probable-deadlock failure.
4. Validators must compare semantics rather than one scheduler-specific trace.
   H2O accepts only complete three-callback groups containing two `H` values
   and one `O`; Bounded Blocking Queue verifies the required dequeue order or
   multiset and final size; Dining Philosophers verifies callback order and
   mutual exclusion; Web Crawler verifies same-host completeness, uniqueness,
   fetch behavior, and scheduler-independent output.
5. `cases.json` must exercise reversed launch orders, staggered and unstaggered
   starts where meaningful, progress, safety, and deadlock-sensitive paths.
   Benchmark inputs stay in `benchmark.json`.

The outer subprocess timeout protects the app. It is not a benchmark verdict.
A correct slower-class implementation must finish every expected output under
the benchmark allowance and fail the fitted scaling verdict.

## Certificate recovery

For a certified package, inspect `complexity_certificate.json` and validate all
of these conditions before touching the blocker record:

- `challenge_id` is the exact `lc_<frontend_id>` identity;
- `required_time` exactly matches the notation in `doc.md`;
- `status` is `verified` and the method is one of `bounded_domain`,
  `bounded_concurrency`, or `asymptotic_optimality`;
- bounded methods include a positive, source-derived `workload_bound`;
- every method-specific replacement check required by
  `engine/complexity_certificates.py` is present with concrete evidence; and
- `benchmark.json` is absent or incomplete, because a completed benchmark and
  completed certificate must not coexist.

The certificate is package-level evidence about the legal complexity-checking
method. User code must still pass all ordinary cases. Real-test must return
`runtime_check: false`, `complexity_check: true`, the exact certificate method,
and a certificate-specific message; the UI must not display fabricated timing
tiers.

Regression coverage belongs in
`server/tests/test_complexity_certificates.py`. Preserve the exhaustive checks
for the tractable finite domains, certificate-schema rejection tests, audit
integration, and one real-test pass for every certified reference. Problem
1165 has a useful correctness trap: the reversed keyboard with word `leetcode`
has expected distance `50`, not `49`.

## Scaling-benchmark recovery

For IDs 1115, 1116, 1117, 1195, and 1242:

1. Preserve the reviewed tier sizes in the resolution map unless fresh timing
   evidence proves that the environment has materially changed.
2. Keep `size` tied to the stated workload symbol at all three tiers, with
   source-valid inputs and hidden expected results.
3. Use semantic validators for scheduler-independent outputs such as H2O and
   Web Crawler; do not force a single thread interleaving.
4. Run the optimal reference and an independently structured implementation in
   the required class; both must pass.
5. Run the correct principal slower class named in the table. It must return
   every expected result, then fail extra growth. A wrong answer, deadlock,
   timeout, or largest-tier safety-cap failure is not valid calibration.

If calibration fails, first check the source-native runner, semantic validator,
and workload construction. Do not enlarge inputs beyond source constraints,
lower the documented complexity, or convert the package to a certificate just
to make the report green.

## Audit and blocker-clearing procedure

Start by refreshing the audit and reading the per-package JSON entry:

```powershell
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py
Get-Content dsa\leetcode\_reports\two_sum_migration_progress.md
```

Then run the focused recovery checks:

```powershell
.\.venv\Scripts\python.exe -m pytest server\tests\test_complexity_certificates.py server\tests\test_special_environments.py server\tests\test_validated_cases.py -q
.\.venv\Scripts\python.exe tools\check_leetcode_dataset.py
```

Clear a blocker only after the refreshed JSON entry has `local_complete: true`,
the original LeetCode-native source remains remotely verified in
`submission.json`, and the relevant focused tests pass:

```powershell
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py --clear-block <frontend_id>
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py
```

Finish with the repository regressions required by `AGENTS.md`, including the
full Python suite, Ruff, web and Electron builds, and `git diff --check`. The
reviewed resolved checkpoint is 1267 fully complete, 1254 scaling benchmarks,
13 certificates, zero blockers, and frontend ID 1268 next. Treat the live
audit as authoritative if those numbers later advance.

## Invalid shortcuts

Never resolve one of these blockers by:

- clearing its record while `local_complete` is false;
- inventing illegal oversized inputs to manufacture scaling;
- substituting a generic certificate waiver for method-specific evidence;
- counting a timeout or safety cap as a slower-class scaling failure;
- weakening semantic validators to accept incomplete or unsafe concurrency;
- changing frontend IDs, source-native class contracts, or required complexity;
  or
- inferring remote verification from local correctness.
