## General

After exactly $k$ operations, original chocolate $j$ has type $(j+k)\bmod n$. Therefore target type $i$ can be obtained from any original index `i`, `i - 1`, ..., `i - k` modulo $n$, depending on the stage at which that chocolate is collected. Its cheapest available purchase cost is the minimum over those $k+1$ sources.

Enumerate $k$ from zero through $n-1$. More operations are unnecessary because after $n$ rotations the type assignment repeats, while the extra operation cost is positive. Keep an array `cheapest` whose entry for each target type is its minimum source cost seen up to the current rotation count.

When increasing the count from $k-1$ to $k$, only the newly reachable source `(type - k) % n` needs to be compared with each stored minimum. The total for this choice is `k * x + sum(cheapest)`. Taking the least total over all counts considers every useful operation schedule, and the per-type minima can be collected at their corresponding stages because purchases do not interfere with one another.

## Complexity detail

There are $n$ useful operation counts, and each count updates $n$ target types and sums their current minima. The running time is $O(n^2)$. The `cheapest` array contains $n$ values, using $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Recompute every minimum:** For each rotation count, scanning all prior sources separately for every type is correct but takes $O(n^3)$ time.
- **Simulate only the cheapest chocolate:** Different target types may have different cheapest sources, so one global source is insufficient.
- **Use more than n rotations:** Type assignments repeat after $n$ operations and `x` is positive, so further rotations can only add cost.
- Zero operations must be considered because immediate purchases may already be optimal.
- With one chocolate, the answer is its purchase cost regardless of `x`.
- Equal purchase costs receive no benefit from rotation.
- Intermediate totals can reach roughly $n\cdot10^9+n\cdot10^9$, so fixed-width implementations need 64-bit arithmetic.
