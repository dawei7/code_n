## General

Let $n$ be the length of `nums`. For the $j$-th selected subarray, define its fixed coefficient as

$$
w_j = (-1)^{j+1}(k-j+1).
$$

**Separate a finished prefix from an active final subarray.** After processing an array prefix, let `best[j]` be the maximum strength obtainable with exactly $j$ selected subarrays anywhere in that prefix. Let `ending[j]` be the maximum strength under the additional requirement that the $j$-th subarray ends at the most recently processed element. These two states distinguish skipping an element from extending a contiguous subarray.

**Update the active subarray.** When the current value is $x$, a solution whose $j$-th subarray ends here has exactly two possibilities. It can extend a previously active $j$-th subarray, adding $w_jx$ to `ending[j]`, or it can start the $j$-th subarray at $x$, adding $w_jx$ to a prior solution represented by `best[j - 1]`. Therefore the update is `ending[j] = max(ending[j] + contribution, best[j - 1] + contribution)`, where `contribution = w_j * x`.

After that transition, `best[j]` is the larger of its old value, which skips $x$, and the new `ending[j]`, which includes $x$. Initialize `best[0] = 0`; every state using at least one subarray starts at negative infinity because no non-empty subarray exists before any element is processed.

**Preserve disjointness with descending updates.** Process $j$ from $k$ down to $1$. Then `best[j - 1]` still describes only earlier array elements when it starts a new subarray at $x$. The same element cannot enter both the $(j-1)$-st and $j$-th subarrays, and every new subarray begins after the preceding one ends. This enforces non-empty, disjoint subarrays in their original left-to-right order.

For each prefix, the two states include every valid choice: the current element is skipped, extends the active final subarray, or starts a new one after a valid smaller state. Induction over the processed positions and selected count therefore shows that `best[k]` is the maximum strength of exactly $k$ valid subarrays after the full array is processed.

## Complexity detail

Each of the $n$ values updates $k$ selected-count states in constant time, giving $O(nk)$ time. The two arrays `best` and `ending` each contain $k+1$ values, so the auxiliary space is $O(k)$.

## Alternatives and edge cases

- **Three-dimensional dynamic programming:** Tracking position, selected count, and whether a subarray is open expresses the same recurrence directly but uses $O(nk)$ space instead of rolling the position dimension.
- **Enumerating all interval endpoints:** Trying every possible next subarray produces a much slower recurrence with at least an extra factor of $n$ and is infeasible near $nk=10^6$.
- **Prefix sums with endpoint enumeration:** Prefix sums make each interval sum constant-time, but they do not remove the quadratic number of candidate intervals per DP layer.
- **Descending selected-count order:** Updating upward would let the current element contribute to `best[j - 1]` before starting state $j$, incorrectly reusing one index in two subarrays.
- **Exactly k non-empty subarrays:** Initialize unreachable states to negative infinity; zero would incorrectly permit missing subarrays, especially on all-negative inputs.
- **Unused elements:** Retaining the old `best[j]` allows gaps before, between, and after selected subarrays.
- **Large magnitudes:** Strength may exceed 32-bit range, so fixed-width implementations require 64-bit integers.
- **k equals one:** The recurrence becomes the ordinary maximum-subarray recurrence, including the requirement to choose a non-empty subarray.
