## General

**Translate an assignment into a completion time**

If a job has workload `a` and its worker completes `b` units per day, the number of whole days needed is

`ceil(a / b)`.

Integer arithmetic computes this as

`(a + b - 1) // b`

for positive `a` and `b`. Adding `b - 1` ensures any positive remainder rounds the quotient upward, while an exactly divisible workload remains unchanged.

All workers operate on their assigned jobs in parallel. The entire collection is finished only when the slowest assigned pair finishes, so an assignment's objective value is the maximum of these rounded-up pair durations.

The problem is therefore a bottleneck matching problem: pair each workload with one daily capacity so that the largest ratio is as small as possible.

**Sort jobs and workers in the same order**

The code sorts `jobs` and `workers` independently in ascending order and pairs entries at equal indices. The smallest job goes to the slowest worker, the next-smallest job to the next-slowest worker, and the largest job to the fastest worker.

This may initially seem counterintuitive because one might want to give the fastest worker a small job so it finishes almost immediately. That would leave a large job for a slower worker, which can make the maximum completion time much worse. Since the objective cares only about the last completion, comparable ranks should be matched.

For the second example, sorted jobs are `[3, 9, 15, 18]` and sorted capacities are `[1, 3, 5, 6]`. Their rounded times are `3, 3, 3, 3`, so every job finishes within three days.

**An exchange argument removes crossed assignments**

Consider two jobs with `a <= A` and two workers with `b <= B`. A crossed assignment gives small job `a` to fast worker `B` and large job `A` to slow worker `b`. Its maximum includes

`ceil(A / b)`.

If the pairs are aligned instead, the two times are `ceil(a / b)` and `ceil(A / B)`. Both are at most `ceil(A / b)`:

- `a <= A` implies `ceil(a / b) <= ceil(A / b)`;
- `B >= b` implies `ceil(A / B) <= ceil(A / b)`.

Therefore aligning this pair cannot make the local maximum larger than the crossed assignment's local maximum. It also leaves all other assignments unchanged.

Whenever an assignment has a faster worker paired with a smaller job while a slower worker has a larger job, this exchange can remove the inversion without increasing the global maximum. Repeating the process eventually produces the sorted-to-sorted pairing. Hence some optimal assignment has exactly the order used by the solution.

**Take the bottleneck among the aligned pairs**

After sorting, `zip(jobs, workers)` yields every aligned workload-capacity pair `(a, b)`. The generator calculates the rounded duration for each, and `max` returns the number of days required by the slowest pair.

That maximum is achievable because all those assignments can run simultaneously and every pair finishes within it. The exchange argument proves no other one-to-one pairing can have a smaller maximum. The returned value is therefore the minimum number of days needed for all jobs.

**A feasibility view gives the same ordering**

For a proposed deadline `D`, worker capacity `b` can finish any job with workload at most `D \cdot b`. Sorting both lists checks the most constrained worker against the smallest remaining job, then moves upward. If sorted pairing fails at some index, there are too many jobs larger than what the corresponding slow workers can handle; rearranging cannot repair that deadline.

The direct sorted maximum computes the smallest successful deadline without an outer binary search. The exchange proof is the compact reason this direct calculation works.

**The exact source sorts in place**

`jobs.sort()` and `workers.sort()` mutate both caller-provided lists. Their original order is irrelevant to the returned optimum, but callers that need to preserve it would have to pass copies or use `sorted`. This side effect is part of the exact implementation.

## Complexity detail

Let `n` be the number of jobs and workers. Sorting each length-`n` list costs `O(n \log n)` time. The zipped generator and maximum scan take `O(n)` additional time, so sorting dominates and total time is `O(n \log n)`.

Python's list sort is in-place from the caller's perspective but may allocate temporary merge storage. Its worst-case auxiliary space is `O(n)`. The generator itself is lazy and holds only one pair and duration at a time, adding `O(1)` beyond sorting workspace.

The input values are positive, so division by zero cannot occur and the ceiling formula is valid. The largest numerator `a + b - 1` is well within the source bounds, and Python integers avoid overflow in any case.

## Alternatives and edge cases

- **Binary search on the number of days:** For each deadline, sort once and test whether each aligned job satisfies `job <= days * worker`. This is correct but adds a logarithmic search that the direct maximum of aligned durations avoids.
- **Priority-queue assignment:** Repeatedly choose a worker for a job based on a local ratio. This adds `O(n \log n)` machinery and requires a proof equivalent to the sorted exchange property.
- **Pair largest job with slowest worker:** Opposite-order pairing maximizes tension and can greatly increase the bottleneck; it is the opposite of the proven alignment.
- **Pair smallest job with fastest worker:** This creates a crossing whenever a larger job is left for a slower worker. Exchanging those two pairs cannot worsen and often improves the maximum.
- **Minimize the sum of completion times:** That is a different objective. The current proof specifically minimizes the maximum pair duration.
- **Use ordinary floor division `a // b`:** It undercounts whenever `a` is not divisible by `b`. Whole days require ceiling division.
- **Floating-point ceiling:** `ceil(a / b)` works for these small bounds but introduces unnecessary floating-point conversion. The integer formula is exact.
- **One job and one worker:** Sorting changes nothing, and the result is the ceiling of their single ratio.
- **Equal workloads:** Their relative order is irrelevant; pairing worker capacities in ascending order still yields the same multiset of durations.
- **Equal worker capacities:** Any order among those workers is equivalent because they take the same time for a given job.
- **Worker faster than job size:** The ceiling duration is one, not zero, because a positive job still needs one day.
- **Exact divisibility:** When `a` is a multiple of `b`, adding `b - 1` does not push integer division into the next quotient.
- **All pairs finish at the same time:** The maximum equals that common duration, as in the balanced second example.
- **Input mutation:** Both input lists are reordered in ascending order. This does not affect correctness but is observable after the call.
- **Nonempty guarantee:** `max` receives at least one generated duration because the arrays have equal positive length.
