## General

**Turn proximity to thieves into a value on every cell.** For any cell, define its cell safeness as the Manhattan distance to the nearest thief. A path's safeness factor is then the minimum cell safeness along that path. The problem asks for a path from the top-left to the bottom-right that maximizes this minimum, often called a maximum-bottleneck path.

The exact solution separates the task into two phases. First, a multi-source breadth-first search computes every cell's nearest-thief distance. Second, cells are activated from safest to least safe, and a union-find structure detects the highest distance threshold at which the endpoints become connected.

This second phase is not the maximum-bottleneck Dijkstra search named by the manifest. It solves the same bottleneck problem through offline threshold connectivity.

**Return zero immediately when an endpoint is a thief.** If `grid[0][0]` or `grid[n - 1][n - 1]` is one, every path includes that endpoint and therefore includes a cell at distance zero from a thief. No safeness factor can exceed zero, and zero is attainable because movement through thief cells is allowed. The early return is both correct and avoids unnecessary preprocessing.

**Run BFS from all thieves at once.** The code initializes `dist` to infinity and enqueues every thief, setting each thief's distance to zero. All thief cells are simultaneous BFS sources.

The direction tuple `(-1, 0, 1, 0, -1)` combined with `pairwise` produces the four moves $(-1,0)$, $(0,1)$, $(1,0)$, and $(0,-1)$. Whenever BFS reaches an in-bounds neighbor whose distance is still infinity, it assigns one plus the current distance and enqueues it.

In an unweighted four-neighbor grid, BFS processes cells in nondecreasing path length from the source set. The first time a cell is reached is therefore the length of a shortest path from any thief. Grid path length under four-direction movement equals Manhattan distance when no obstacles exist, and thieves do not block movement for this distance calculation. Hence `dist[i][j]` becomes exactly the minimum Manhattan distance to any thief.

**Interpret a safeness threshold as an induced graph.** Fix a number $d$. Keep only cells with `dist >= d` and the grid edges between adjacent kept cells. There exists a path with safeness factor at least $d$ exactly when the start and destination are connected in this threshold graph.

As $d$ decreases, more cells become eligible and connectivity can only increase. The desired answer is the greatest threshold at which the two endpoints are connected.

**Activate cells from high distance to low distance.** The code creates triples `(dist[i][j], i, j)` for all $n^2$ cells and sorts them in reverse order. It then processes one triple at a time. Conceptually, a processed cell is active, while cells appearing later are not active yet.

For the current cell with distance `d`, the code examines each neighbor and unions them when `dist[x][y] >= d`. Why is comparing the neighbor's distance enough even without a separate active array? Because sorting is descending. Every cell with greater distance has already been processed. A cell with equal distance may appear earlier or later due to tuple tie-breaking, but unioning it early is still safe: it is already eligible at the same threshold $d$, and its own later processing will merely add any remaining same-threshold edges. No cell below $d$ can be unioned.

After all cells of threshold at least $d$ that matter to a connection have been linked, union-find components represent connectivity using only cells whose safeness is at least $d$. The code checks endpoint roots after each processed cell. The first time they match, the current `d` is returned.

**Why checking inside an equal-distance group is safe.** Suppose several cells share distance $d$. Processing one can union it with an equal-distance neighbor that has not yet had its own turn, effectively activating that neighbor slightly early. This cannot create a path using a distance below $d$, because that neighbor itself has distance exactly $d$. If connectivity appears midway through the group, its bottleneck is still at least $d$, and the returned numeric threshold is correct.

**How union-find maintains components.** Each cell maps to integer `i * n + j`. Initially, every identifier is its own parent. `find` follows parent pointers to a representative and compresses the traversed path. `union` finds both representatives and attaches the smaller component to the larger according to `size`, keeping trees shallow. If the roots already agree, no work is needed.

**Why the first connection gives the maximum.** Before the algorithm reaches distance $d$, it has used only cells with distances strictly greater than $d$, and the endpoints were not connected or the method would already have returned. When they first connect while processing $d$, there is a path whose every cell has distance at least $d$. Thus safeness $d$ is attainable, while every greater threshold was unattainable. This proves $d$ is exactly the maximum safeness factor.

**Endpoint distance bounds every answer.** Any path includes both endpoints, so its safeness cannot exceed either endpoint's nearest-thief distance. The descending activation automatically respects that fact: an endpoint cannot participate in a connection before its threshold is reached.

## Complexity detail

Let $N=n^2$ be the number of grid cells. Multi-source BFS enqueues each cell once and examines four edges per cell, taking $O(N)$ time and $O(N)$ space for the distance matrix and queue.

Creating and sorting the $N$ triples takes $O(N \log N)$ time and $O(N)$ space. The activation phase considers at most four neighbors per cell and performs $O(N)$ union-find operations. With path compression and union by size, their total time is $O(N\alpha(N))$, where $\alpha$ is the inverse Ackermann function and is effectively constant. Sorting dominates, so total time is $O(N \log N)$.

The distance matrix, sorted triples, BFS queue, parent array, and size array each use $O(N)$ storage. Total auxiliary space is $O(N)$. In terms of side length, these bounds are $O(n^2 \log n)$ time and $O(n^2)$ space, since $\log(n^2)$ differs from $\log n$ only by a constant factor.

The manifest's summary names Dijkstra, but its stated $O(N \log N)$ time and $O(N)$ space still match this sorting-plus-union-find implementation.

## Alternatives and edge cases

- **Maximum-bottleneck Dijkstra:** After the same distance BFS, use a max-heap keyed by the best path bottleneck to each cell. Pop the safest available state and relax a neighbor with the minimum of the current bottleneck and the neighbor's cell safeness. This also takes $O(N \log N)$ time.
- **Binary search plus BFS:** Test whether endpoints connect using only cells with distance at least a threshold. Monotonicity permits binary search, producing $O(N \log n)$ time after preprocessing.
- **Bucket activation:** Nearest-thief distances are bounded by $2n-2$, so cells can be grouped by integer distance and processed without comparison sorting, potentially reducing the second phase to near-linear time.
- **Start or destination is a thief:** The answer is zero because every path includes a zero-distance cell; the source handles this before BFS.
- **One-cell grid:** The constraint guarantees at least one thief, so its only cell is a thief and the early return gives zero.
- **Multiple thieves:** Enqueuing all of them before BFS makes the first arrival select the nearest one automatically.
- **Paths may cross thieves:** Such a path has bottleneck zero. The graph does not forbid thief cells; it assigns them distance zero.
- **Equal-distance activation:** Unioning a not-yet-iterated neighbor with the same threshold is safe because eligibility is defined by value, not processing order.
- **No explicit active array:** The descending sort plus `dist[neighbor] >= d` condition is the activation test. Reversing the sort would invalidate this reasoning.
- **Four-direction movement:** Diagonal cells are not adjacent. The direction encoding yields exactly the allowed Manhattan neighbors.
- **Union-find indexing:** Mapping $(i,j)$ to `i * n + j` is one-to-one for an $n$ by $n$ grid.
