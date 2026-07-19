## General
**Which costs every direct route must pay**

To change from `startRow` to `homeRow`, the robot must enter every intervening row once in the appropriate direction. The starting row is excluded and the home row is included. The same rule independently applies to columns. Therefore, a monotone route has a fixed cost: the sum of those required row entries plus those required column entries.

**Why detours cannot improve the answer**

All entry costs are nonnegative. Any route that reverses vertical or horizontal direction enters at least one row or column more times than a monotone route. Removing such a detour cannot increase the cost. Consequently, some optimal route moves only toward the destination on each coordinate, and the order in which its vertical and horizontal moves are interleaved is irrelevant.

**Summing in both directions**

Choose a row step of `1` when home is below the start and `-1` when it is above. Begin one row beyond the start and continue through the home row, adding each entry cost. Repeat the same process for columns. When a coordinate already matches, its range is empty and contributes zero.

## Complexity detail
Exactly $D$ required row and column entries are visited, so the running time is $O(D)$. The algorithm stores steps, indices, and a running total only, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Shortest-path search:** Dijkstra's algorithm can model every grid cell, but it ignores the separable destination-entry costs and is far more expensive than necessary.
- **Prefix sums:** Precomputed row and column prefix sums answer each interval in $O(1)$ time, but constructing them costs $O(m+n)$ time and space for a single query.
- **Enumerating complete paths:** Different monotone move orders all pay the same required entries, so path enumeration adds combinatorial work without changing the cost.
- If start and home are equal, no cost is paid even when their row and column costs are positive.
- Moving upward or left still charges the row or column being entered, not the one being left.
- Zero-cost entries may make detours equally cheap, but never strictly cheaper than a direct monotone route.
