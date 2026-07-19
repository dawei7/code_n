## General
**Propagate excess instead of retained liquid**

Keep the amount arriving at each glass in the current row. A glass retains at most one cup, so only `max(0, amount - 1) / 2` flows into each child. Adding this overflow to positions `j` and $j + 1$ of the next row automatically combines contributions from the two parents of an interior glass.

**Stop at the queried row**

Begin with `[poured]` for row zero and build one new row at a time until reaching `query_row`. Every transfer uses only the completed row above, so earlier rows can be discarded. Return the queried arrival amount capped at one.

For row zero, the stored amount is exactly what was poured. If a stored row is correct, applying the capacity rule to every glass sends exactly half of each excess along each downward edge; summing at the child therefore gives its exact incoming amount. Induction makes the queried row correct, and capping its arrival models the glass's capacity.

## Complexity detail
Let `r = query_row`. The algorithm processes $1 + 2 + \ldots + r$ glasses, taking $O(r^2)$ time. It stores only the current and next rows, each of length at most $r + 1$, for $O(r)$ auxiliary space.

## Alternatives and edge cases
- **In-place reverse update:** A single length-$r + 2$ array can be updated from right to left, preserving the same time and space bounds with fewer allocations.
- **Full triangular table:** Storing every row makes the recurrence visually direct but uses $O(r^2)$ space when only one queried row is needed.
- **List-backed recursive memoization:** Caching states in per-row lists is correct, but linearly searching those lists adds another factor of `r` to the work.
- **Uncached recursion:** Computing both parent amounts recursively repeats the same subproblems and can take exponential time.
- **No overflow:** If a glass receives at most one cup, it contributes zero to both children.
- **Edge glasses:** They have only one possible parent, while interior glasses combine two contributions.
- **Overfilled query:** Return `1.0`, not its total incoming amount.
- **Top glass:** For `query_row = 0`, the result is simply `min(1, poured)`.
