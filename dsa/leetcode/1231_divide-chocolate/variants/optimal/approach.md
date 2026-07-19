## General
**Search the guaranteed sweetness rather than the cuts.** Suppose every piece must have total sweetness at least a candidate value `minimum`. Scan the chunks from left to right, accumulating a running sum. Whenever that sum reaches `minimum`, finish the current piece immediately and reset the sum. Because every chunk has positive sweetness, taking the earliest possible boundary leaves the greatest possible suffix for later pieces. This greedy scan therefore creates the maximum number of qualifying pieces for that candidate.

**Use monotonic feasibility.** If the scan creates at least `k + 1` pieces, exactly `k + 1` pieces can be obtained by merging any surplus adjacent pieces; merging cannot lower their sweetness. Thus `minimum` is feasible. If the greedy scan creates fewer pieces, no later placement of a boundary could create more, so the candidate is impossible. Every value below a feasible candidate is also feasible, while every value above an impossible candidate is impossible.

**Binary-search the last feasible value.** The answer is at least `min(sweetness)`: greedily ending a piece whenever it reaches that value always yields at least one piece per chunk when necessary. It is at most `S // (k + 1)`, since `k + 1` pieces cannot all exceed their average. Search this inclusive integer interval with an upper midpoint. On feasibility, retain `mid` and move the lower bound to it; otherwise set the upper bound to `mid - 1`. The interval terminates at the greatest feasible minimum, which is precisely the optimal guaranteed sweetness.

## Complexity detail
Each feasibility test scans all $n$ chunks in $O(n)$ time. The initial search interval has width at most $S/(k+1)$, so binary search performs $O\left(\log\frac{S}{k+1}\right)$ tests. The scan uses only counters and a running sum, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate cut positions:** Trying every choice of `k` boundaries is exact but requires $\binom{n-1}{k}$ partitions in the worst case.
- **Dynamic programming over prefixes and cuts:** Recording the best minimum for every prefix and piece count is correct but takes substantially more than linear work per search decision.
- **Scan every candidate sweetness:** Testing each integer through `S // (k + 1)` preserves correctness but can take pseudo-polynomial time instead of logarithmically many scans.
- **No cuts:** When `k = 0`, the only piece is the whole bar and the answer is $S$.
- **One chunk per piece:** When `k = n - 1`, every chunk stands alone and the answer is `min(sweetness)`.
- **Surplus greedy pieces:** More than `k + 1` qualifying pieces is sufficient because adjacent pieces may be merged without violating the minimum.
- **Positive values:** Positivity is what makes an earliest qualifying cut safe and the feasibility predicate monotone under the greedy construction.
