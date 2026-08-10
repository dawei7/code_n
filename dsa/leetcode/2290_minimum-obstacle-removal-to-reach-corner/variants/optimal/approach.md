## General

**Turn the grid into a zero-or-one weighted graph**

Treat every cell as a graph vertex. Orthogonally adjacent cells have directed moves in both directions. Entering an empty cell costs zero obstacle removals; entering a cell containing one costs one because that obstacle must be removed.

The requested answer is therefore the minimum path cost from the upper-left vertex to the lower-right vertex in a graph whose edge weights are only zero and one.

The starting cell contributes no cost. The contract guarantees it is empty, and the initial deque entry is `(0, 0, 0)`, where the third value is the accumulated removal count.

**Why a deque replaces a priority queue**

Ordinary breadth-first search works only when every edge has the same cost. Dijkstra's algorithm works here, but a binary heap is more machinery than weights zero and one require.

Zero-one BFS maintains pending states in nondecreasing cost order with a deque:

- moving into a zero cell preserves cost, so the new state goes to the front;
- moving into an obstacle adds one, so the state goes to the back.

The code uses `appendleft` for the first case and `append` for the second. This scheduling ensures all states reachable at the current cost are processed before states that require an additional removal.

**Store coordinates and cost together**

Each deque item is `(i, j, k)`: row, column, and the cost of the path that enqueued it. Popping from the left chooses the smallest pending cost under the zero-one ordering.

The direction tuple `(-1, 0, 1, 0, -1)` combined with `pairwise` produces up, right, down, and left. Bounds checks reject coordinates outside the rectangular grid.

For an in-bounds neighbor `(x,y)`, its new cost is `k` when `grid[x][y] == 0` and `k+1` otherwise.

**Finalize a cell only when it is popped**

The exact source does not maintain a distance matrix and does not prevent duplicate enqueueing. A cell may enter the deque through several neighboring paths.

`vis` records cells whose minimum cost has been finalized. When a popped coordinate is already in `vis`, that duplicate state is skipped. Otherwise, it is added to `vis` and its neighbors are expanded.

This is safe because the deque discipline makes the first popped entry for a cell have minimum possible cost. Any later entry for the same coordinate has cost no smaller and cannot improve a route that can continue from the already finalized state.

**Why first pop has minimum cost**

Assume states already popped had nondecreasing costs. From a state of cost `k`, zero-cost neighbors are placed before all currently pending cost-`k+1` work, while one-cost neighbors join the back. No newly generated state can cost less than `k`.

Consequently, a cell cannot first be popped with cost `c` while an undiscovered path of cost below `c` is still waiting behind it. That cheaper path's zero and one transitions would have been scheduled earlier. This is the specialized Dijkstra correctness argument for weights zero and one.

**Return as soon as the destination is popped**

The destination check occurs immediately after popping and even before the duplicate-visited check. Because every popped state appears in nondecreasing cost order, the first destination entry has optimal cost and may be returned at once.

A later duplicate destination entry cannot have a smaller value. No full traversal or separate final-distance lookup is needed.

**Why the infinite loop terminates**

The code uses `while 1` rather than testing whether the deque is nonempty. In a rectangular grid, every cell is geometrically reachable from every other through orthogonal moves. Obstacles may be removed rather than acting as permanent walls, so some finite-cost route to the destination always exists.

The destination will therefore be enqueued and popped before the deque could become empty.

**Trace free and costly choices**

From a current cell with cost two, an empty neighbor is placed at the front with cost two. It will be considered before an obstacle neighbor placed at the back with cost three. A chain of empty cells continues at the front, allowing the search to exhaust all reachable cost-two territory before committing to another removal.

This behavior finds a path with fewer obstacles even when that path uses more physical steps. The optimization target is removal count, not path length.

**Why revisiting coordinates is unnecessary after finalization**

Once a cell is reached at minimum removal cost, every future continuation depends only on that coordinate and cost. A higher-cost arrival cannot produce a cheaper complete path, because all remaining edge costs are nonnegative. Skipping later copies is therefore correct.

The grid itself is never changed. “Removing” an obstacle is represented only by paying its entry cost; revisiting the same obstacle on a path would never help a minimum nonnegative-cost route.

## Complexity detail

Let `V = mn` be the number of cells. The grid graph has `O(V)` edges because every cell has at most four neighbors.

Each coordinate is expanded once after joining `vis`. The source may enqueue duplicates before finalization and may enqueue already visited neighbors, but every expansion examines only four edges, so total enqueues remain `O(E)=O(V)`. Deque operations are constant time. Total time is `O(mn)`.

The visited set and deque can each hold `O(mn)` entries, giving `O(mn)` auxiliary space. Unlike the editorial version, the exact source allocates no distance matrix.

## Alternatives and edge cases

- **Dijkstra with a heap:** It is correct for nonnegative weights but takes `O(mn\log(mn))` time rather than exploiting the two possible costs.
- **Ordinary FIFO BFS:** It prioritizes number of moves, not obstacle removals, and can return a shorter but more expensive path.
- **Distance-matrix zero-one BFS:** It avoids some duplicate entries through relaxation checks; the exact source instead finalizes with a visited set.
- **Mark visited on enqueue:** That is unsafe in weighted search because a cheaper route may be discovered before the first queued copy is popped.
- **No obstacles needed:** A zero-cost chain reaches the destination and returns zero.
- **Obstacle neighbor:** It is placed at the back with cost increased by one.
- **Empty neighbor:** It is placed at the front with unchanged cost.
- **Duplicate deque entries:** Only the first non-destination pop expands the cell; later copies are skipped.
- **Destination duplicate:** The first popped destination is already optimal, so the early return is safe.
- **One row or one column:** The same graph interpretation follows the only geometric corridor.
- **Guaranteed empty endpoints:** No cost is paid at the start, and the destination itself never requires removal.
- **Cycles:** The visited set prevents repeated expansion despite four-way movement.
- **Input preservation:** Obstacles are modeled as costs and `grid` is not mutated.
