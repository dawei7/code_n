## General

This grid contains two kinds of transitions with different costs:

- moving to an orthogonally adjacent non-obstacle cell costs one move;
- teleporting between cells with the same uppercase letter costs zero moves.

An ordinary breadth-first search is designed for edges that all have the same cost, so it cannot directly prioritize a free teleport over a one-move step. Dijkstra’s algorithm would work, but a priority queue is more machinery than necessary because every edge weight is either zero or one. The solution uses **0-1 BFS**, a specialized shortest-path algorithm for exactly these two weights.

**Modeling the grid as a graph**

Treat every traversable cell as a graph vertex. Up, down, left, and right moves create weight-one edges when the destination is inside the grid and is not `'#'`. If several cells contain the same letter, any one of them can teleport to any other at weight zero while that letter is available.

The answer is the shortest-path distance from vertex `(0, 0)` to vertex `(m - 1, n - 1)`. This graph interpretation is valuable because “minimum number of moves” becomes a standard shortest-path question, while free teleports explain why edge weights are not uniform.

**Collecting portal groups before the search**

The dictionary `g` maps each uppercase letter to the coordinates carrying that letter. The initial double loop visits every grid cell once and appends portal coordinates to their group. Empty cells and obstacles are not added.

This preprocessing allows the search to find all zero-cost destinations of a portal immediately. Without it, reaching a letter would require rescanning the entire grid to locate matching cells, potentially repeating that expensive scan many times.

The check `c.isalpha()` identifies the portal cells under the stated input alphabet. The constraints promise uppercase English letters, dots, or hash marks, so alphabetic cells are precisely portals.

**How 0-1 BFS orders work**

The matrix `dist` starts at infinity everywhere except `dist[0][0] = 0`. The deque `q` initially contains only the start.

When a transition improves a distance, its destination is scheduled according to its edge cost:

- a zero-cost teleport is inserted with `appendleft`, at the front;
- a one-cost grid move is inserted with `append`, at the back.

This maintains the key 0-1 BFS ordering: work reachable at the current distance is handled before work that costs one more move. It plays the same role as Dijkstra’s minimum-priority extraction, but a deque is enough because there are only two possible increments.

When `(i, j)` is popped, the source reads `d = dist[i][j]`. It does not store an old distance inside the deque entry. If a coordinate was scheduled and later improved before being processed, the pop therefore uses its newest, smaller distance. Relaxation still occurs only for a strict improvement, so equal-distance discoveries do not cause pointless reinsertions.

**Relaxing free portal transitions**

Let `c = matrix[i][j]`. If `c` remains in `g`, this is the first time its portal group is expanded. For every coordinate `(x, y)` carrying that letter, the algorithm tests whether the current distance `d` improves `dist[x][y]`. An improvement costs nothing, so the new distance is `d` and the cell goes to the front of the deque.

Afterward, `del g[c]` removes the group. This does not mean the algorithm incorrectly consumes a portal for every possible route. It is a search optimization based on shortest-path order.

The first popped cell of letter `c` has the smallest possible distance at which any `c` portal can be reached. From that cell, every other `c` cell can be reached immediately for the same distance. Therefore the first expansion assigns the best distance obtainable through this letter to the entire group. If the search later reaches another `c` cell with distance `d' \ge d`, expanding the group again could offer only `d'` to cells that already received at most `d`. It cannot improve anything.

There is also no need to represent “used letters” as an exponential path state. Suppose a route appears to teleport with the same letter more than once. All cells of that letter form a zero-cost complete connection: the route could teleport directly from its first occurrence to the last same-letter destination and omit the intermediate uses. Thus an optimal route never needs more than one use of a particular letter, consistent with the statement.

Deleting the group is what keeps the algorithm linear. A letter may occupy many cells. If its full list were scanned from every such cell, one large portal group could cause quadratic work.

**Relaxing ordinary moves**

The tuple `dirs = (-1, 0, 1, 0, -1)`, together with `pairwise(dirs)`, generates the four direction pairs:

`(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`.

For each pair, the code forms neighbor `(x, y)` and checks three requirements:

1. the row is in `[0, m)`;
2. the column is in `[0, n)`;
3. the destination is not an obstacle.

If `d + 1` is smaller than the recorded neighbor distance, the algorithm updates it and appends the neighbor at the back because this edge costs one move. Notice that the current cell does not need a separate obstacle check: only reachable, enqueued cells are processed, and obstacle destinations are never enqueued.

**Why returning when the target is popped is safe**

0-1 BFS processes vertices in nondecreasing shortest-distance order. All zero-cost continuations of distance `d` are placed before any pending distance-`d + 1` work. Consequently, when the destination reaches the front and is popped, no undiscovered route with a smaller cost can remain behind it. Returning `d` at that moment is therefore safe.

If the deque becomes empty first, every cell reachable through any legal combination of moves and teleports has been explored. An infinite target distance then means no route exists, so the method returns `-1`.

**Example of a free start teleport**

For `matrix = ["A..", ".A.", "..."]`, the start itself is portal `A` at distance zero. Expanding `A` gives `(1, 1)` distance zero and pushes it to the front. From there, two ordinary moves reach `(2, 2)`, so the returned answer is `2`. Teleportation does not add one to the distance, and the deque placement faithfully enforces that rule.

## Complexity detail

Let `N = mn` be the number of grid cells. Building portal groups scans all `N` cells once, taking `O(N)` time.

During 0-1 BFS, each processed cell considers at most four ordinary neighbors. A successful relaxation can schedule a cell again if its distance improves, but for a graph with weights zero and one, the total relaxation work is linear in the numbers of vertices and represented edges. The grid contributes `O(N)` neighbor edges.

Each portal list is expanded exactly once because its dictionary entry is deleted immediately afterward. Across all letters, the lists contain at most `N` coordinates, so all portal-loop iterations together cost `O(N)` rather than `O(N^2)`. The overall time complexity is therefore `O(mn)`.

The distance matrix stores one value per cell, portal groups store at most one coordinate entry per portal cell, and the deque can contain `O(mn)` scheduled coordinates. Thus the auxiliary space complexity is `O(mn)`.

## Alternatives and edge cases

- **Dijkstra’s algorithm:** A binary-heap shortest-path search correctly handles zero- and one-cost edges and is easier to generalize to larger weights, but it costs `O(mn \log(mn))` here. 0-1 BFS exploits the restricted weights to obtain linear time.
- **Ordinary BFS:** Treating teleports and grid steps identically would charge the wrong cost, while processing free portal destinations without deque priority can finalize cells in the wrong order. Plain BFS is suitable only when every edge costs the same amount.
- **Explicit portal-clique edges:** Connecting every pair of equal-letter cells makes the graph conceptually direct, but a group of `k` portals would create `O(k^2)` edges. Storing each group once and expanding it once represents the same useful reachability in linear total work.
- **State including a used-letter mask:** Such a state is unnecessary and could multiply the search space by `2^{26}`. Any repeated use of one letter can be compressed into a single free jump between the first and final same-letter cells.
- **One-time group deletion:** Removing `g[c]` is safe only because the first expansion occurs at the minimum reachable distance and reaches the entire same-letter group at zero cost. This shortest-path argument is the reason the optimization is correct.
- **A portal appearing once:** Its group expansion checks only that same cell and creates no useful transition. Deleting the group still prevents repeated work.
- **Starting on a portal:** The source may teleport before making any ordinary move, because the start is processed at distance zero.
- **Starting at the destination:** In a `1 x 1` grid, the first popped coordinate is already the bottom-right cell, so the method returns zero even if that cell contains a portal.
- **Obstacle destination:** Obstacles are never enqueued as ordinary-move destinations. If the bottom-right cell is an obstacle in an input beyond the stated practical assumptions, it is unreachable unless it is also the start, which cannot simultaneously be `'#'` because the start is guaranteed non-obstacle.
- **Unreachable open regions:** The deque eventually empties after exploring the start’s entire reachable component, and `-1` is returned.
- **Multiple shortest routes:** Strict improvement checks avoid rescheduling a cell for an equal distance. Keeping one shortest distance is sufficient; the problem asks only for the minimum count, not for the number or reconstruction of shortest routes.
- **Large portal groups:** Every coordinate in the group is scanned together only once, which is essential for grids as large as `10^3 x 10^3`.
- **Portal-letter semantics:** The proof relies on every occurrence of a letter being mutually reachable by one free teleport. If portals instead formed directed pairs or charged different costs, the group-expansion model would need to change.
