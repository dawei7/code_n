## General
**Give every first-group point one mandatory edge.** Because all costs are non-negative, an optimal solution never needs two edges from a first-group point merely to satisfy that point itself. Process the first group in order and choose one second-group endpoint for each point. A bitmask records which second-group points these mandatory choices have covered. Different choice histories with the same row index and mask have identical remaining obligations, so only their cheapest cost matters.

**Repair uncovered second-group points at the end.** After all $m$ rows have chosen an edge, some second-group bits may still be absent. For each uncovered point $j$, add its cheapest incident edge, `min(cost[i][j])`. These repairs are independent: they may attach to any already processed first-group point, and adding them cannot make another uncovered point covered. Precompute each column minimum so the terminal cost is quick to evaluate.

This construction represents an optimum. From any feasible connection set, select one incident edge for every first-group point as its mandatory edge; the remaining selected edges include coverage for every still-uncovered second-group point and cost at least that point's column minimum. Conversely, every DP choice plus the terminal repairs covers both groups. Minimizing over all mandatory choices and using the cheapest possible repairs therefore yields exactly the global minimum.

## Complexity detail
There are at most $(m+1)2^n$ states `(i, mask)`. Each nonterminal state tries $n$ endpoints, giving $O(mn2^n)$ time. The memoized states use $O(m2^n)$ space, while the recursion depth is $O(m)$ and the column-minimum array uses $O(n)$ additional space.

## Alternatives and edge cases
- **Enumerate one endpoint assignment per first-group point:** This tries $n^m$ assignments before repairing uncovered columns, repeating many equivalent `(i, mask)` states.
- **Minimum-cost matching:** Requiring one-to-one pairs is too restrictive because a point may need multiple incident edges and $m$ can exceed $n$.
- **Full edge-subset enumeration:** Testing all $2^{mn}$ subsets is correct but ignores the small second-group dimension that makes bitmask DP practical.
- Zero-cost edges are valid and can make the total answer `0`.
- When $n=1$, every first-group point must connect to the single second-group point, so every row's only cost is included.
- A second-group point omitted by all mandatory choices still needs its cheapest extra edge, even if that attaches to a first-group point that already has another connection.
