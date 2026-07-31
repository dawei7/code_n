## General

**Compress all paths ending in one row**

For each column of the current row, store the minimum cost of any path ending
there, including that cell's value. The first row initializes these costs with
its own values because a path may start in any column and has not moved yet.

**Relax every transition to the next row**

For a current column with cell value `v` and accumulated cost `costs[j]`,
consider every destination column `c`. Reaching the next-row cell costs
`costs[j] + moveCost[v][c] + grid[next_row][c]`. Keep the smallest candidate
for each destination, then replace the current cost vector.

The stored value for a destination is minimal because every possible
predecessor is examined and the recurrence adds exactly the required move cost
and newly visited value. Induction over rows therefore preserves the cheapest
path to every cell. The minimum cost in the final vector is the cheapest path
ending anywhere in the last row.

## Complexity detail

There are $m-1$ transitions between rows, and each transition considers all
$n^2$ predecessor-destination pairs, for $O(mn^2)$ time. Two length-$n$ cost
vectors suffice, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Enumerate complete paths:** Trying every next-row column produces $n^m$ possible paths and repeats shared prefixes.
- **Memoized top-down search:** Caching the best suffix from each cell gives the same $O(mn^2)$ time with $O(mn)$ memo and recursion space.
- **Shortest-path algorithm:** The grid induces a layered acyclic graph, so general Dijkstra machinery is unnecessary.
- **Arbitrary starting column:** Initialization must include every first-row cell, not just the top-left cell.
- **Arbitrary destination column:** The answer is the minimum over the entire last row.
- **Value-indexed costs:** `moveCost` is indexed by the current cell's value, not its column.
- **Cell values:** Both the starting cell and every destination cell contribute to the path total.
- **Last row:** Its `moveCost` entries are never used because the path stops there.
