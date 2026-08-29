## General

**Why searching the whole grid is impossible**

The grid has `10^6 \times 10^6` cells, so an ordinary search from source to target could examine up to a trillion positions. The key constraint is not grid size but the number of blocked cells: at most 200.

Such a small set of obstacles cannot form an enormous closed wall. It can only trap an endpoint inside a bounded region whose area is quadratic in the number of blockers. Once a search visits more cells than any possible enclosed region, it has proved that its start is not trapped. It does not need to continue all the way across the grid.

**The enclosure limit**

Let `B = len(blocked)`. Arranging blockers diagonally against a grid boundary is the most efficient way to surround many open cells with few blocked cells. The resulting triangular region has on the order of

$$
\frac{B(B-1)}{2}
$$

reachable cells. A fully interior enclosure cannot beat the same quadratic scale because it needs blocked cells around all sides.

The code uses the conservative threshold

`m = B^2 // 2`.

This is at least as large as the standard maximum finite enclosure bound. Therefore, if a search visits more than `m` distinct cells, those cells cannot all lie inside a region sealed by the available blockers. The starting endpoint has escaped any possible blockade.

The threshold is a proof cutoff, not an estimate of the source-to-target distance. The endpoints may be hundreds of thousands of coordinates apart, yet exploring only about 20,001 cells is enough when `B = 200`.

**Blocked and visited sets**

`s = {(x, y) for x, y in blocked}` converts blocked coordinates to tuples in a hash set. Membership checks then take expected constant time.

Each bounded DFS receives its own `vis` set. A coordinate is added as soon as its call begins. This prevents cycles and makes `len(vis)` the number of distinct open cells reached from that endpoint.

Source and target searches use separate visited sets because each must independently prove that its own endpoint is not enclosed.

**Three ways one search can finish**

The helper `dfs(source, target, vis)` returns true in either of two success cases.

First, after adding the current cell, if `len(vis) > m`, the search has exceeded the maximum possible enclosure. The start is not trapped, so this directional check succeeds even if the distant target has not yet been visited.

Second, while examining neighbors, if `[x, y] == target`, a concrete open path has reached the target and success is immediate.

If neither happens and every reachable neighbor is exhausted, the helper returns false. That means the explored region is finite, has size at most the threshold, and does not contain the target. Its start is enclosed away from the target.

**Explore legal neighbors**

The tuple `dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` produce offsets for up, right, down, and left.

A neighbor is explored only when:

- Both coordinates lie from zero through `10^6 - 1`.
- Its tuple is not in the blocked set `s`.
- It has not already been visited in this search.

These are exactly the movement rules. Python's short-circuit evaluation ensures set lookups and recursion happen only after bounds are valid.

**Why checking only the source side is insufficient**

Suppose the source is in the large open region but the target is sealed inside a tiny ring of blocked cells. A source search quickly exceeds the threshold and returns true without ever reaching the target. That proves only that the source is not trapped; it does not prove the target is reachable.

The final expression therefore requires both:

`dfs(source, target, set()) and dfs(target, source, set())`.

The reverse search detects whether the target is trapped. Python short-circuits `and`, so if the source search already proves impossibility, the reverse work is skipped.

If an actual path is found in either direction, reachability is symmetric because moves are undirected. The second check will also succeed, either by finding the endpoint or escaping its threshold.

**Why two non-enclosed endpoints can meet**

With only `B <= 200` blocked cells in a million-wide grid, blockers cannot form a wall spanning the entire board. They can separate cells only by creating small finite enclosures. Outside those enclosures is one vast connected open region.

If both directional searches exceed the enclosure limit, both endpoints belong to this common exterior region and a path exists between them. If either endpoint is inside a sealed finite component not containing the other, its directional DFS exhausts that component below the threshold and returns false.

This is the core logical alternative: reach the other endpoint directly, or prove membership in the common large exterior.

**Trace the blocked corner**

For blocked cells `[0,1]` and `[1,0]` with source `[0,0]`, the source is at a grid corner. North and west leave the grid, while its only in-grid neighbors are blocked.

The search adds `(0,0)` to `vis`. The threshold for two blockers is two, so one visited cell does not exceed it. No legal neighbor exists, and DFS returns false. The final `and` stops and the method correctly reports that target `[0,2]` is unreachable.

**No blocked cells**

When `B = 0`, `m = 0`. The first DFS adds its starting cell, making `len(vis) = 1 > 0`, and returns true immediately. The reverse search does the same.

With no obstacles, every two grid cells are connected by horizontal and vertical moves, so this constant-work result is correct.

**Why the target comparison uses a list**

Neighbor coordinates are computed as integers `x` and `y`. The target parameter is a two-element list, so the code compares `[x, y] == target`. Blocked and visited membership use tuples because tuples are hashable. These different representations serve their respective operations without changing coordinate meaning.

**Why the answer is correct**

If either directional DFS returns false, its endpoint lies in an exhausted open component that neither contains the other endpoint nor exceeds the enclosure bound. No path can leave that component, so the endpoints are disconnected.

If both return true, each endpoint either directly reached the other or proved it is not inside any finite blocker enclosure. Direct reach is conclusive. Otherwise both lie in the common large exterior component, so they are connected. The conjunction therefore returns true exactly for reachable endpoint pairs.

## Complexity detail

Let `B` be the number of blocked cells. The threshold is `O(B^2)`. Each directional DFS visits at most the finite enclosed region or stops as soon as its visited count becomes `m + 1`. Each visited cell checks four neighbors, so both searches together take `O(B^2)` time.

The blocked set uses `O(B)` space. A visited set contains at most `O(B^2)` coordinates, and recursive depth can also reach that order in the worst traversal shape. Total auxiliary space is `O(B^2)`, matching the manifest.

The bounds deliberately do not depend on the million-cell side length. That independence is the point of the enclosure argument.

## Alternatives and edge cases

- **Full-grid BFS or DFS:** It is logically correct but computationally impossible on up to `10^{12}` cells. The blocker-derived cutoff is essential.
- **Bounded breadth-first search:** A queue can perform the same two directional checks and stop after more than `m` discoveries. It avoids recursion-depth risk and has the same `O(B^2)` bounds.
- **Coordinate compression:** Compress rows and columns around obstacles and endpoints, preserving gaps between significant coordinates. This can solve the problem but requires careful treatment of large empty intervals and adjacency.
- **Search only from source:** This misses a target enclosed in a small region while the source is outside. Both directions are necessary.
- **Zero blockers:** Threshold zero makes both checks succeed immediately, which is correct for an open grid.
- **One blocker:** A single cell cannot enclose either endpoint, so the threshold also permits immediate escape proof.
- **Corner enclosure:** Grid boundaries act like free walls, allowing very few blocked cells to trap a corner. The DFS bounds checks and finite-region exhaustion detect it.
- **Target reached before cutoff:** The helper returns true immediately because a concrete path is stronger evidence than the enclosure argument.
- **Source and target far apart:** Distance does not increase the bounded search once both endpoints are known to be outside small enclosures.
- **Blocked coordinates as tuples:** Hash-set membership requires immutable tuple keys; visited coordinates use the same representation.
- **Separate visited sets:** Reusing the source set for the reverse check would not prove independent escape and could skip necessary exploration.
- **Grid outer boundary:** Coordinates equal to `-1` or `10^6` are rejected, so searches never leave the legal board.
- **Recursive implementation:** The mathematical cutoff can still exceed Python's default recursion depth. An iterative queue or stack preserves the algorithm when runtime stack limits are a concern.
- **Conservative threshold:** `B^2 // 2` may allow slightly more exploration than the tight triangular bound, but exceeding it still safely proves non-enclosure.
