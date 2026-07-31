## General

Operations at one string position never alter any other position, so the global optimum is the sum of the cheapest transformation for each pair `(s[i], t[i])`. Between two letters on the alphabet cycle there are two simple routes: repeatedly move forward, or repeatedly move backward. Because every edge cost is nonnegative, adding an extra full cycle cannot improve either route.

Build one prefix sum over `nextCost` and one over `previousCost`. For a forward route that does not cross `z` to `a`, subtract two forward-prefix entries. If it wraps, combine the suffix from the source to `z` with the prefix from `a` to the target.

Backward edges require careful indexing: leaving letter $j$ toward $j-1$ costs `previousCost[j]`. Thus a non-wrapping backward route from source index $a$ to target index $b\le a$ costs the prefix interval from $b+1$ through $a$. When $b>a$, combine the interval from $a$ down through zero with the interval from 25 down through $b+1$.

For each aligned character pair, compute these two route costs in constant time and add the smaller one. This is optimal per position, and independence makes the sum optimal for the whole string.

## Complexity detail

Building the two 26-letter prefix arrays takes constant time, and each of the $n$ string positions is processed once. Total time is $O(n)$ and auxiliary space is $O(1)$ because the alphabet has fixed size 26.

Runtime scaling cannot distinguish the natural direct-walk alternative: it performs at most 25 steps per character and is also linear under the fixed lowercase-alphabet contract. The verified `asymptotic_optimality` certificate therefore replaces a benchmark. Any correct algorithm has a worst-case $\Omega(n)$ input-inspection lower bound, which the accepted implementation matches.

## Alternatives and edge cases

- **Walk the alphabet for every pair:** Simulating at most 25 forward and 25 backward edges is correct and remains $O(n)$ for the fixed alphabet, but prefix sums remove that repeated constant work.
- **All-pairs shortest paths:** Floyd-Warshall on 26 letters also works, yet it obscures the fact that only the two directed routes on one cycle can be optimal.
- **Dijkstra per distinct source letter:** Nonnegative edges make it valid, but a heap is unnecessary on this two-neighbor cycle.
- **Identical letters:** Both prefix differences are zero, so that position contributes nothing even when all edge costs are positive.
- **Wrapped edge indexing:** `z` to `a` uses `nextCost[25]`, while `a` to `z` uses `previousCost[0]`.
- **Zero-cost edges:** A longer route may beat the direct route, including at total cost zero.
- **Large totals:** Costs up to $10^9$ across $10^5$ positions can exceed 32-bit integer range.
