## General

**Interpret equal-character neighbors as an undirected graph**

Treat each grid cell as a graph vertex. Two vertices share an undirected edge when their cells are vertically or horizontally adjacent and contain the same character.

The question then becomes ordinary cycle detection in an undirected graph. A valid grid cycle uses at least four cells because an orthogonal grid graph is bipartite and has no triangle; immediately returning along the same edge is explicitly forbidden.

The source explores every equal-character connected component with a depth-first traversal implemented by a Python list.

**Track both the cell and its parent**

Each stack entry is `(x, y, px, py)`:

- `x, y` are the current row and column.
- `px, py` are the cell from which the traversal entered it.

When inspecting neighbors, the algorithm skips `(px, py)`. In an undirected graph, every edge appears in both directions. Without this parent exception, the current cell would see the vertex it just came from as already visited and incorrectly report a two-step return as a cycle.

Any different already-visited same-character neighbor represents an alternate connection within the explored component and therefore closes a genuine cycle.

**Start one traversal per unvisited component**

The outer loops visit every grid coordinate. If `vis[i][j]` is already true, that cell belongs to a component explored earlier and is skipped.

For a new root, the source marks it visited and pushes `(i, j, -1, -1)`. Negative parent coordinates cannot match any valid cell, so the root has no excluded neighbor.

The list is named `q`, but `q.pop()` removes from its end. It therefore behaves as a LIFO stack and produces depth-first traversal rather than queue-based breadth-first traversal. Either traversal order supports the same undirected-cycle rule.

**Generate the four directions compactly**

`dirs = (-1, 0, 1, 0, -1)` combined with `pairwise(dirs)` generates:

- Up: `(-1, 0)`.
- Right: `(0, 1)`.
- Down: `(1, 0)`.
- Left: `(0, -1)`.

For each direction, `nx, ny` is checked against row and column bounds before any grid access.

The exact source relies on `pairwise` being available from the runtime's iterator utilities.

**Stay inside one character component**

Every traversal root has character `grid[i][j]`. A candidate neighbor is ignored when `grid[nx][ny] != grid[i][j]`.

Although the variable name `x` initially holds the outer-loop character and is later reused as the popped row coordinate, comparison explicitly reads `grid[i][j]`. The root character therefore remains available through the grid and is not lost by variable shadowing.

Because traversal crosses only same-character edges, every reached cell necessarily matches that root character.

**Mark cells when pushing them**

An unseen valid neighbor is marked `True` before it is appended. This prevents multiple frontier cells from independently scheduling the same cell as if it were undiscovered.

If a later edge encounters that already-marked cell and it is not the current parent, the two frontier routes establish a cycle. Mark-on-push detection is correct for this undirected graph and avoids duplicate stack entries.

**Why a non-parent visited neighbor proves a cycle**

During traversal, parent pointers form a tree of discovery edges. There is exactly one tree path between any two discovered vertices.

Suppose current vertex `u` has an equal-character edge to visited vertex `v` that is not `u`'s parent. That edge is not merely the reverse of the discovery edge. Combining it with the existing discovery-tree path between `u` and `v` forms a closed route.

In a simple orthogonal grid, that route has at least four edges, so it satisfies the problem's length requirement.

**Why every cycle is detected**

Consider any same-character cycle. The first traversal reaching it builds discovery edges through some of its vertices. Eventually it examines a cycle edge whose other endpoint has already been discovered through the other direction around the cycle.

That endpoint is not merely the current cell's parent, so the algorithm returns true.

If all components finish without such an edge, every same-character component's processed edges form a forest. A forest contains no cycle, so returning false is correct.

**No recursive stack risk**

The grid can contain 250,000 cells. Recursive DFS in Python could exceed the recursion limit on a long component.

The explicit list stack stores traversal frames on the heap and avoids that language-level recursion-depth problem.

## Complexity detail

Let $R$ and $C$ be grid dimensions. Every cell is marked at most once and, when popped, examines exactly four directions. Total time is $O(RC)$, matching the manifest.

The visited matrix contains $RC$ Booleans. In the worst case, the explicit stack can also hold $O(RC)$ entries. Auxiliary space is $O(RC)$.

Direction storage and scalar coordinates use constant additional space.

## Alternatives and edge cases

- **Recursive DFS:** It uses the same parent rule but risks Python recursion overflow on a large component.
- **Breadth-first search:** A deque with parent coordinates is equally correct; traversal order does not affect detection.
- **Union-find:** Process each equal-character edge once and report a cycle when endpoints are already connected. It uses $O(RC)$ storage.
- **Skip no parent edge:** That would falsely call every ordinary undirected edge a cycle.
- **Single cell:** It has no edge and returns false.
- **One row or one column:** The graph is a path or disjoint paths, so no valid cycle exists.
- **Different neighboring characters:** No graph edge connects them.
- **Large uniform rectangle:** The traversal quickly encounters a non-parent visited neighbor and returns true.
- **Diagonal equality:** Diagonal cells are not adjacent and create no edge.
- **Multiple components:** The outer loops start a fresh traversal for each unvisited one.
- **Mark on push:** It prevents duplicate scheduling and makes frontier cross-edges visible as cycles.
- **Minimum cycle length:** Orthogonal grid structure rules out a same-character triangle, while parent skipping rules out immediate two-edge backtracking.
- **Iterator dependency:** `pairwise(dirs)` must be supplied by the execution environment exactly as the stored source expects.
