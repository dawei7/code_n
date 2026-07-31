## General

Only bases from $1$ through $m = \lfloor n^{1/x} \rfloor$ can participate, because every larger $x$-th power already exceeds the target. This turns the problem into counting subsets of the distinct values $1^x, 2^x, \ldots, m^x$ whose sum is exactly `n`.

Let `dp[total]` be the number of subsets of the powers processed so far that sum to `total`. Initially, the empty subset is the sole way to make zero, so set `dp[0] = 1`. For each new `power`, every existing subset summing to `total - power` produces one subset summing to `total` by including that power. Add `dp[total - power]` into `dp[total]`, reducing the count modulo $10^9 + 7$.

**Why totals must be visited in descending order**

Process `total` from `n` down to `power`. Then `dp[total - power]` still describes subsets formed before the current power was introduced. Each update therefore either omits the power or includes it exactly once. An ascending loop would make a just-updated state available again during the same iteration and could count the same base repeatedly, violating uniqueness.

After all eligible powers are processed, every subset of distinct positive bases has been considered once. The state `dp[n]` consequently counts exactly the required sets, independent of the order in which their members might be listed.

## Complexity detail

Let $m = \lfloor n^{1/x} \rfloor$. Each of the $m$ eligible powers scans at most `n` totals, so the running time is $O(nm)$. The one-dimensional table contains `n + 1` counts and uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Two-dimensional subset-sum DP:** Record a row for every eligible base. This makes the include-or-omit recurrence explicit but uses $O(nm)$ space without improving the $O(nm)$ running time.
- **Memoized include-or-skip recursion:** Cache states by base index and remaining sum. It has comparable polynomial state count, but adds recursion and memo-table overhead.
- **Unmemoized subset enumeration:** Try both choices for every eligible base. It is correct, but its $O(2^m)$ running time scales much worse than the dynamic program.
- **Descending update order:** Reversing the inner loop to ascending order changes the task into an unbounded-count problem and incorrectly permits repeated use of a base.
- **Single-base representation:** A target that is itself an $x$-th power contributes the singleton set containing that base.
- **No representation:** If no subset reaches `n`, `dp[n]` remains zero.
- **Modulo reduction:** Counts must be reduced during transitions; for example, the maximum first-power target already has enough distinct-part partitions to exceed the modulus before reduction.
