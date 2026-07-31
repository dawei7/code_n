## General

Color the chessboard by the parity of $x+y$. Cells with an even sum have one color, and cells with an odd sum have the other.

A knight move changes one coordinate by two and the other by one, so it changes the coordinate sum by an odd number. Every move therefore switches colors. After an even number of moves the knight must be on its starting color, while after an odd number it must be on the opposite color.

The standard $8\times8$ knight graph is connected, so every target cell is reachable from every start cell. Because the graph is bipartite under this coloring, all paths between a fixed pair of cells have the same length parity. Thus an even-length route exists exactly when `start` and `target` have equal coordinate-sum parity. The zero-move route also correctly handles identical cells.

## Complexity detail

The algorithm reads four coordinates and performs a fixed number of additions, remainder operations, and one comparison. It takes $O(1)$ time and $O(1)$ auxiliary space.

The legal board contains only 64 cells and 4,096 ordered start-target pairs. This fixed domain is why the package uses a bounded-domain complexity certificate rather than artificial scaling tiers.

## Alternatives and edge cases

- **Breadth-first search with move parity:** Search states `(x, y, parity)` over at most 128 combinations. This is also constant on the fixed board but obscures the coloring invariant and uses a queue and visited set.
- **Shortest-path distance only:** Computing one shortest distance is sufficient here because every path between the same two cells has the same parity in the bipartite knight graph, but full distance computation is unnecessary.
- **Identical cells:** Zero moves is even, and both coordinate sums are necessarily equal.
- **One legal knight move:** The destination has the opposite color, so the result is `false`.
- **Board boundaries:** The parity argument does not enumerate moves and works unchanged for corners and edges; connectivity of the complete standard board supplies sufficiency.
