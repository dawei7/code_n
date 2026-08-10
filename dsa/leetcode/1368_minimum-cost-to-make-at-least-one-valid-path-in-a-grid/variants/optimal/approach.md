## General

**See the grid as a graph with only zero-cost and one-cost edges**

Treat every cell as a graph node. From a cell, there is an edge to each in-bounds neighbor: right, left, down, and up. Taking the edge named by the current cell's sign costs zero because no modification is needed. Taking any of the other three edges costs one because the sign must be changed to point that way.

The original problem is therefore a shortest-path problem from cell `(0, 0)` to cell `(m - 1, n - 1)`. A path's total edge weight is the number of signs that must be changed along that path. All weights are either zero or one, which permits 0–1 breadth-first search instead of a general priority queue.

The `dirs` array has a dummy entry at index zero so its useful indices match the grid values exactly. Index one is right, two is left, three is down, and four is up. Thus `grid[i][j] == k` means moving in direction `k` costs zero.

**Why a deque replaces a normal queue**

The deque stores triples `(row, column, distance)`. The start enters as `(0, 0, 0)`. When a move follows the current arrow, the new triple has the same distance and is inserted with `appendleft`. It should be processed immediately because it costs no more than the current path. A move that changes the arrow has distance `d + 1` and is inserted with ordinary `append`, behind all currently available paths of the smaller cost.

This front-versus-back rule keeps pending states ordered by nondecreasing cost in the way needed for weights zero and one. It is the two-bucket equivalent of Dijkstra's priority queue: zero-weight relaxations remain in the current cost layer, while one-weight relaxations wait for the next layer.

**Why the first processed copy of a cell is final**

The code does not maintain a full distance matrix. Different neighbors may enqueue the same cell, perhaps with different distances. The `vis` set resolves those duplicates when they are removed from the deque. If a coordinate is already visited, that queued copy is skipped. Otherwise, the coordinate is marked visited and its distance becomes final.

This is safe because 0–1 BFS removes states in nondecreasing distance order. The first removed copy of a cell cannot have a more expensive cost than some copy still waiting behind it. Therefore no later route can improve the finalized cost. Marking at removal time, rather than insertion time, is important: a cell may first be discovered through a cost-one edge and then be reached more cheaply through a chain of zero-cost edges before the expensive copy is processed.

Once the bottom-right cell is removed for the first time, `d` is its shortest distance, so the method returns immediately. Continuing the traversal could finalize other cells but could not lower the target's cost.

**Why edge costs represent legal sign changes**

For a chosen simple path, each departed cell needs to point only to the next cell on that path. If its original sign already does, its contribution is zero; otherwise changing it once is sufficient and contributes one. Nonnegative shortest paths never need a cycle: removing a repeated-cell cycle cannot increase cost. Hence an optimal route can be taken as simple and never requires assigning two different outgoing signs to the same cell. The graph model therefore respects the rule that a cell's sign may be modified at most once.

Signs pointing outside the grid cause no special case. The loop generates only in-bounds neighbors. Since none of those directions equals the outward sign's effective move, leaving that cell through any legal neighbor costs one.

**Why the algorithm is correct**

Every legal movement between adjacent cells appears as one graph edge, and its edge weight equals exactly whether that cell's sign must change. Thus every grid path maps to a graph path of the same modification cost, and every graph path describes a feasible sequence of grid moves with that cost after cycle removal.

The deque rule processes zero-cost continuations before cost-one continuations, so states are finalized in nondecreasing total cost. The first visit of every cell consequently records its minimum possible path cost. In particular, when the target is first visited, its attached `d` is the minimum number of modifications needed to create at least one valid path. That is the requested answer.

The final `return -1` is defensive. Because every cell connects to its in-bounds neighbors and the rectangular grid is connected when directions may be changed, the target is always reachable under the stated constraints.

## Complexity detail

Let $R$ and $C$ be the row and column counts. There are $RC$ cell nodes and at most four outgoing edges per node. A coordinate is expanded only once because `vis` rejects later copies. Its expansion checks four directions, so useful processing is $O(RC)$. Duplicate queued entries are also bounded by the constant number of incoming grid edges, keeping total deque work $O(RC)$.

The visited set contains at most $RC$ coordinates, and the deque can also hold $O(RC)$ entries. Therefore auxiliary space is $O(RC)$. These bounds match the Optimal manifest. Each deque operation is $O(1)$ amortized; using a binary heap would add an unnecessary logarithmic factor.

## Alternatives and edge cases

- **Dijkstra with a heap:** General shortest-path logic also works because weights are nonnegative, but it costs $O(RC\log(RC))$ rather than exploiting the zero-or-one weights.
- **Distance-grid 0–1 BFS:** Store the best cost per cell and enqueue only genuine improvements. This avoids some duplicates and makes relaxation explicit; the exact code instead finalizes the first deque removal with `vis`.
- **Layered DFS plus BFS:** Follow all free arrows to fill one cost layer, then pay one modification to seed the next layer. It can also be linear but requires coordinating two traversal styles.
- **One-cell grid:** The start is already the target. Its initial triple is removed and returns zero before examining neighbors.
- **Already valid route:** Repeated zero-cost moves are pushed to the front, allowing the target to be reached with distance zero.
- **Outward-pointing sign:** No invalid coordinate is enqueued. Every legal departure from that cell is treated as a one-cost change.
- **Duplicate queue entries:** They are expected and harmless. Only the first removed copy expands the cell; `vis` discards the rest.
- **Visited timing:** Marking a cell when enqueued would be unsafe because a later zero-cost route could improve it before removal.
- **Cycles of free arrows:** The visited set prevents infinite traversal. Removing a cycle never hurts a minimum-cost route.
- **Input mutation:** The method reads direction values but never changes `grid`; the returned number describes the minimum hypothetical modifications.
- **Direction numbering:** The unused `dirs[0]` is deliberate. Removing it without subtracting one from grid values would map every arrow incorrectly.
