## General
**Treat pairs as strict intervals**

A pair can follow the current chain exactly when its left endpoint is greater than the last chosen right endpoint. This is the same compatibility condition as interval scheduling, with touching endpoints considered overlapping because the inequality is strict.

**Consider the earliest finishing pair first**

Sort pairs by their right endpoint. Scan in that order and select a pair whenever it starts after the current chain end, then replace the chain end with that pair's right endpoint.

**Why the earliest finish is safe**

Among all pairs that could be chosen next, the one with the smallest right endpoint leaves at least as much space for every later pair as any alternative. Replacing the next pair in an optimal chain with this earliest-finishing compatible pair cannot invalidate the remainder or reduce its length.

**Extend the exchange argument repeatedly**

After choosing the earliest finisher, the remaining problem is identical but restricted to pairs starting after its end. Applying the same exchange argument at each step constructs a chain whose length matches an optimal chain.

## Complexity detail
Sorting `N` pairs costs $O(N \log N)$, and the greedy scan costs $O(N)$. Creating the sorted copy uses $O(N)$ auxiliary space; the scan itself stores only the last endpoint and count.

## Alternatives and edge cases
- **Quadratic dynamic programming:** sort by a coordinate and compute the best chain ending at each pair; it is correct but takes $O(N^2)$ time.
- **Sort by starts and replace the current end:** keep the smaller right endpoint whenever pairs overlap; this is an equivalent greedy formulation.
- **Backtracking over pair orders:** explores exponentially many subsets and permutations.
- Pair order in the input has no effect because reordering is allowed.
- Equality is not compatible: `[1,2]` cannot precede `[2,3]`.
- Negative endpoints obey the same strict comparison.
- Nested long pairs should be skipped in favor of shorter, earlier-finishing choices.
- Duplicate pairs can contribute at most one position at the same boundary because they overlap.
