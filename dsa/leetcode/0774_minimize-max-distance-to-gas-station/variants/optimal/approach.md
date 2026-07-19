## General
**Test whether a maximum gap is feasible**

For an original interval of length $g$, keeping every new segment at most $D$ requires $\lceil g/D\rceil$ pieces and therefore $\lceil g/D\rceil-1$ new stations. Sum this requirement over all original gaps; $D$ is feasible exactly when the total is at most $k$.

**Binary-search the answer value**

The feasibility predicate is monotone: increasing `D` never requires more stations. Start with lower bound zero and upper bound equal to the largest original gap. At each iteration, test their midpoint. A feasible midpoint becomes the new upper bound; an infeasible one becomes the lower bound. A fixed number of iterations shrinks the interval far below the accepted tolerance.

Every value below the true optimum is infeasible and every value at or above it is feasible. The binary-search invariant keeps the optimum between the two bounds, with the upper bound feasible. Once the bounds are sufficiently close, returning the upper bound approximates the minimum feasible distance to the required precision.

## Complexity detail
Let `n` be the station count, `R` the largest original gap, and `epsilon` the target precision. Each feasibility check scans $n - 1$ gaps, and binary search performs $O(\log(R / \varepsilon))$ checks, for $O(n \log(R / \varepsilon))$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Maximum heap of current segment lengths:** Add stations one at a time to the interval with the largest current segment; it is exact but costs $O((n + k) \log n)$ time.
- **Enumerate station allocations among gaps:** This can prove tiny cases but grows combinatorially with `k` and the number of intervals.
- **Integer-only binary search:** It cannot represent arbitrary real station positions or fractional answers.
- **One original gap:** The answer is its length divided by $k + 1$.
- **Exact divisibility:** A gap already split into exact length-`D` pieces needs one fewer station than the piece count.
- **Unused capacity:** If a candidate needs fewer than `k` stations, extra stations can be placed without increasing its maximum gap.
- **Floating-point comparison:** Results within the accepted tolerance represent the same optimum.
