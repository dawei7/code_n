## General

**Why the fixed-window trick is no longer enough**

Candidate subarrays may have any length of at least `k`. Their denominators are therefore different, so the largest sum does not necessarily give the largest average. A long subarray can have a larger sum but a smaller average than a short one. Recomputing and comparing every legal subarray would examine quadratically many candidates.

The optimal approach instead asks a yes-or-no question: for a proposed average `v`, does any subarray of length at least `k` have average at least `v`? This feasibility question can be answered in one linear scan. Because feasibility changes monotonically as `v` changes, binary search can locate the maximum feasible value.

**Bound the answer**

The average of any nonempty subarray is a weighted combination of its elements, so it cannot be smaller than the minimum array value or larger than the maximum array value. The search interval therefore begins with:

- `l = min(nums)` as a certainly feasible lower bound;
- `r = max(nums)` as an upper bound on every possible average.

The lower bound is feasible because every element is at least the minimum, so every legal subarray also has average at least that minimum. The upper endpoint may or may not be attainable by a length-at-least-`k` subarray, but no answer can exceed it.

**Transform an average condition into a sum condition**

For a candidate `v`, replace every array value conceptually with `nums[i] - v`. For a subarray of length `L`, its transformed sum is:

`original_sum - L * v`.

That transformed sum is nonnegative exactly when:

`original_sum / L >= v`.

Thus `check(v)` only needs to determine whether there is a length-at-least-`k` subarray whose transformed sum is nonnegative. No transformed array is actually allocated; values are subtracted from `v` as they enter running sums.

For example, testing `v = 4` against original values `[3, 6, 5]` produces conceptual values `[-1, 2, 1]`. The last two have transformed sum three, which proves their original average is at least four.

**Check the first eligible window**

The variable `s` initially stores the transformed sum of the first `k` elements:

`sum(nums[:k]) - k * v`.

If `s >= 0`, that first length-`k` window already proves feasibility, so the helper returns `True` immediately.

If not, longer windows and later starting positions must be considered. Doing so efficiently requires transformed prefix sums.

**Use the smallest eligible earlier prefix**

Imagine transformed prefix sum `P[j]` is the sum of transformed elements before index `j`, with `P[0] = 0`. The transformed sum of a subarray from `j` through `i` is:

`P[i + 1] - P[j]`.

For that subarray to contain at least `k` elements, its start must satisfy `j <= i - k + 1`. For a fixed end `i`, the easiest way to obtain a nonnegative difference is to subtract the smallest prefix sum among all eligible starts. Therefore, a valid subarray ending at `i` exists exactly when:

`P[i + 1] >= min(P[0], P[1], ..., P[i - k + 1])`.

The helper maintains these quantities without a prefix array:

- `s` is the current transformed prefix sum `P[i + 1]`;
- `t` advances as the newly eligible lagging prefix `P[i - k + 1]`;
- `mi` is the minimum of all eligible lagging prefixes seen so far.

Both `t` and `mi` begin at zero, representing `P[0]`. When the loop first runs at `i = k`, `s` gains transformed element `k`, while `t` gains transformed element zero and becomes `P[1]`. Taking `mi = min(mi, t)` makes both possible starts zero and one eligible for a window ending at `k`. The test `s >= mi` then checks whether at least one of those windows has nonnegative transformed sum.

On each later iteration, exactly one more start position becomes old enough to form a length-at-least-`k` window. Updating `t` with `nums[i - k] - v` and folding it into `mi` adds that start to the set of eligible prefixes. No earlier minimum is discarded because long subarrays remain permitted.

**Why the feasibility scan is complete**

The initial test handles the only eligible window ending at index `k - 1`. For every later ending index `i`, `mi` contains exactly the minimum transformed prefix among every start that gives length at least `k`. If `s >= mi`, subtracting the prefix that achieved `mi` yields a nonnegative transformed subarray, so a qualifying average exists.

Conversely, if some qualifying subarray ends at `i`, its earlier prefix `P[j]` is in the eligible set. Since `mi <= P[j]` and `P[i + 1] - P[j] >= 0`, it follows that `P[i + 1] >= mi`, so the helper detects feasibility. If no iteration passes, no legal end and start pair has a nonnegative transformed sum. Therefore, `check(v)` is true exactly when the optimum average is at least `v`.

**Why binary search applies**

If an average `v` is feasible, every smaller candidate is also feasible: subtracting a smaller number from each element only increases transformed sums. If `v` is infeasible, every larger candidate is infeasible. Feasible candidates thus form a continuous lower portion of the search interval.

At each midpoint:

- when `check(mid)` is true, the optimum is at least `mid`, so `l` moves up to `mid`;
- when it is false, the optimum is below `mid`, so `r` moves down to `mid`.

The interval always continues to contain the boundary between feasible and infeasible values. Each iteration halves its width. When the width is below `1e-5`, `l` is a feasible lower approximation within the required tolerance of the optimum, so returning `l` is appropriate.

**Why the update order inside `check` matters**

For an end index `i`, the start `i - k + 1` produces a window of exactly length `k` and must already be eligible. The code first updates `t` and `mi`, then performs `s >= mi`. Reversing those steps would omit the newest exact-length candidate at that end and could return a false negative.

Likewise, `mi` must remember the smallest prefix ever eligible, not merely the most recent prefix. Discarding older prefixes would ignore longer subarrays, which are explicitly allowed.

## Complexity detail

Let `N` be the array length, let `R = max(nums) - min(nums)` be the initial numeric range, and let `eps = 1e-5`.

One `check` call computes an initial length-`k` sum and then scans the remaining elements once, taking `O(N)` time. Binary search halves the interval until its width is below `eps`, requiring `O(log(R / eps))` iterations when `R` is positive. The total running time is therefore `O(N log(R / eps))`.

Since the values are bounded, the number of binary-search iterations is also bounded by a modest constant in practice, but retaining the logarithmic expression explains how precision and value range affect the work.

The feasibility logic stores only `s`, `t`, `mi`, and a few loop variables, so the abstract method uses `O(1)` auxiliary space. The exact Python source calls `sum(nums[:k])`, and the slice `nums[:k]` materializes `k` references for each check. Its literal peak auxiliary space is therefore `O(k)`. Replacing the slice with a loop over the first `k` indices keeps the algorithm unchanged and restores strict `O(1)` working space.

No prefix-sum array or transformed array is stored. Floating-point operations introduce small rounding error, which is why the algorithm searches to a specified tolerance instead of expecting exact equality at the optimum.

## Alternatives and edge cases

- **Enumerate all subarrays:** Prefix sums can evaluate each chosen start and end in constant time, but there are quadratically many length-at-least-`k` pairs. That produces `O(N^2)` time and is too slow for the intended constraints.

- **Use only length-`k` sliding windows:** This solves the first maximum-average variant but is incorrect here. A longer subarray can have a higher average than every exact-length-`k` window considered in isolation around a chosen local position.

- **Store a full transformed prefix array:** For each candidate `v`, building all prefix sums and scanning a running minimum is correct in `O(N)` time and `O(N)` space. The exact approach compresses those prefix values into `s`, `t`, and `mi`.

- **Convex-hull or geometric prefix-sum methods:** More advanced techniques can characterize maximum slopes between prefix-sum points and may avoid numeric binary search. They are substantially harder to implement and reason about; the monotone feasibility method is robust and meets the required tolerance.

- **All elements equal:** `l` and `r` start equal, so the binary-search loop does not run. Returning that shared value is exact.

- **`k = N`:** Only the whole array is legal. The feasibility check's initial window decides every candidate, and binary search converges to the whole-array average.

- **`k = 1`:** A single maximum element is legal, so the answer is `max(nums)`. The general transformation and prefix-minimum scan still reaches that result.

- **All values negative:** The initial bounds and transformed sums work without any zero-based assumption. The maximum average may remain negative, and binary search still maintains feasible and infeasible ordering.

- **Mixed signs:** A very negative prefix can make a later long subarray favorable after subtraction. Tracking the minimum eligible prefix is precisely what captures this possibility.

- **First window is feasible:** Returning immediately is correct because `check` asks only whether any qualifying subarray exists, not which one or what its maximum average is.

- **Remembering only the current lagging prefix:** This can miss a longer optimal subarray whose best start occurred much earlier. `mi` must be a cumulative minimum.

- **Using `s > mi` instead of `s >= mi`:** Equality means the transformed subarray sum is zero, which corresponds to an average exactly equal to `v` and must count as feasible.

- **Returning the upper bound:** At termination, `r` may still be slightly infeasible, while `l` is maintained as feasible. Returning `l` gives the safer approximation under the invariant.

- **Floating-point termination:** Testing exact equality between bounds is unreliable. The width comparison against `eps` guarantees progress and a controlled approximation error.

- **Temporary first-window slice:** It does not affect correctness or time complexity, but it makes the exact Python implementation use `O(k)` peak extra memory. An index-based initial sum is required for a literal `O(1)`-space claim.
