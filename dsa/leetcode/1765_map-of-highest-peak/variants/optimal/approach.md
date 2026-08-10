## General

**The greatest legal height is distance to nearest water**

Every water cell must have height zero, and moving across one grid edge can change height by at most one. If a cell is $d$ steps from a water cell, its height can be at most $d$: along that path, starting from zero, height can rise by at most one per step.

The strongest such upper bound comes from the nearest water cell. Therefore every legal assignment satisfies:

$$
\text{height}[i][j]
\le
\operatorname{distanceToNearestWater}(i,j).
$$

Assigning each cell exactly that nearest-water distance is legal. Neighboring cells' distances to the same source differ by at most one, water distances are zero, and all distances are nonnegative. Because this assignment reaches the pointwise upper bound at every cell, it maximizes the highest peak.

The exact solution computes these distances with multi-source breadth-first search.

**Start BFS from every water cell**

`ans` is initialized to minus one in every cell. Minus one means unvisited and cannot be confused with a valid height because heights are nonnegative.

The initialization scan places every water coordinate into deque `q` and sets its answer to zero. Instead of running a separate BFS from every water cell, all sources share one queue. They form distance layer zero simultaneously.

The problem guarantees at least one water cell, so the queue is initially non-empty.

**Generate the four side-sharing neighbors**

The source uses:

`pairwise((-1, 0, 1, 0, -1))`.

Adjacent pairs of this five-value sequence are:

- `(-1, 0)` for up,
- `(0, 1)` for right,
- `(1, 0)` for down,
- `(0, -1)` for left.

For current cell `(i, j)`, adding one pair `(a, b)` produces neighbor `(i + a, j + b)`. Diagonal movement is never generated.

The boundary checks `0 <= x < m` and `0 <= y < n` reject coordinates outside the matrix.

**Assign a cell only on first discovery**

A neighbor is processed only when `ans[x][y] == -1`. Its height becomes:

`ans[i][j] + 1`,

and its coordinate is appended to the queue.

BFS removes coordinates in nondecreasing distance from the source set. Thus the first time a cell is reached, the current path uses the smallest possible number of grid edges from any water cell. Marking it immediately prevents later, longer paths from enqueueing or overwriting it.

Water cells already contain zero, so they are never rediscovered through a neighboring land cell.

**Trace a small grid**

For `[[0,1],[0,0]]`, the water cell at top right enters the initial queue with height zero.

Its left and lower land neighbors are discovered at height one. Processing those distance-one cells discovers the bottom-left cell at height two. Any alternate route to that cell is no shorter, so two is its nearest-water distance.

The result `[[1,0],[2,1]]` satisfies every adjacency bound and has the maximum possible peak two.

**Why adjacent assigned heights differ by at most one**

Nearest-source distance on an unweighted graph is a 1-Lipschitz function. For adjacent cells $u$ and $v$, take a shortest path from $u$ to water. Moving first from $v$ to $u$ gives a path from $v$ whose length is at most $\operatorname{dist}(u)+1$. By symmetry:

$$
\left|\operatorname{dist}(u)-\operatorname{dist}(v)\right|\le 1.
$$

Therefore the BFS distance matrix automatically satisfies the required local height rule.

**Why this assignment maximizes the peak**

For any cell and any path of length $d$ to a water cell, a legal nonnegative height can rise from zero by at most $d$. So no legal solution can assign that cell more than its nearest-water distance.

BFS assigns exactly that distance to every cell. It is therefore not merely one feasible map: no cell can be raised above its assigned value in any feasible map. In particular, no other assignment can have a higher maximum cell, proving optimality.

**Why the returned matrix is complete**

The grid is connected through side adjacency. Starting from at least one water source, BFS eventually reaches every cell. Each is enqueued once, receives one nonnegative height, and remains unchanged afterward. No minus-one entry remains when the queue empties.

## Complexity detail

Let $R=m$ and $C=n$. The initialization scans all $RC$ cells. BFS enqueues and dequeues each cell once and examines four directions per cell. Total time is $O(RC)$.

The output matrix uses $O(RC)$ space, and the deque can hold $O(RC)$ coordinates in the worst case. Thus total storage is $O(RC)$, matching the manifest. Direction generation and scalar coordinates use constant additional space.

The input matrix is read for water locations and is not modified; `ans` is a separate result matrix.

## Alternatives and edge cases

- **Run BFS from each land cell:** It repeats work and can be far slower than one multi-source traversal.
- **Two-pass dynamic programming:** Forward and backward distance passes also achieve $O(RC)$ time with an output matrix, but the BFS proof is more direct for multiple sources.
- **Priority queue:** All grid edges have equal cost, so Dijkstra's heap is unnecessary; an ordinary deque gives linear time.
- **All cells water:** Every cell starts at zero, no new cell is discovered, and the maximum height is zero.
- **Single water cell:** Heights become Manhattan distances from that source.
- **Several water cells:** The first BFS wave to reach a cell comes from a nearest source.
- **One-row grid:** The method reduces to distance along a line.
- **One-column grid:** The same line-distance behavior applies vertically.
- **Water revisited from land:** Its zero marker prevents enqueueing again.
- **Equal shortest paths:** First discovery chooses one path, but only distance matters.
- **Minus-one sentinel:** It is safe because every legal height is nonnegative.
- **Four-direction tuple:** `pairwise` over five values deliberately closes the direction cycle.
- **No diagonal adjacency:** Only side-sharing moves are generated.
- **At least one source:** The stated guarantee ensures every cell receives a finite height.
- **Input preservation:** The returned assignment is independent of the original zero/one storage.
