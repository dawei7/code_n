## General
**Compute the first complete window.** Sum the first `k` entries through a generator over their positions, without materializing an input slice. Compare that total with the two thresholds: subtract one only when it is strictly below `lower`, add one only when it is strictly above `upper`, and otherwise leave the score unchanged.

**Slide without resumming.** When the window moves one position right, add the entering value `calories[right]` and subtract the leaving value `calories[right - k]`. This updates the total in constant time while preserving exactly the sum of the current consecutive `k` days.

Score each updated window with the same strict comparisons. The first window and the $n-k$ subsequent slides cover every valid start exactly once, so the accumulated score matches the required evaluation and can be negative when losses outnumber gains.

## Complexity detail
The generator examines `k` values and the sliding loop processes each remaining value once. Since $k\leq n$, total time is $O(n)$. The generator retains only its current position, while the running sum, score, and loop index are scalars, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Resum every window:** Calling `sum(calories[start:start + k])` is correct but takes $O(nk)$ time and becomes quadratic when $k$ grows with $n$.
- **Slice only the first window:** `sum(calories[:k])` keeps the linear-time sliding algorithm, but the temporary list contains `k` references and therefore uses $O(k)$ auxiliary space rather than the required $O(1)$.
- **Prefix sums:** A length-$n+1$ prefix array gives each window sum in $O(1)$ time and $O(n)$ total time, but uses $O(n)$ extra space.
- **Equality with a threshold:** A total equal to `lower` or `upper` is inside the inclusive no-change range.
- **One-day windows:** With `k = 1`, each array element is scored independently.
- **Whole-array window:** With `k = n`, exactly one total is evaluated.
- **Zero calories:** Zero values participate normally and can make the final score negative.
