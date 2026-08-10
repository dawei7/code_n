## General

**A query asks for a reachable threshold component**

For threshold `v`, a cell can score a point only when its value is strictly less than `v`. Starting at the top-left cell, the maximum score is therefore the number of cells connected to `(0,0)` through four-directional paths whose every cell value is below `v`.

Revisiting cells cannot add points, so the task is a reachability count, not a longest walk.

Larger query thresholds can only add eligible cells; they never remove a previously reachable one. This monotonicity lets all queries share one incremental graph expansion.

**Sort queries but remember their original positions**

`qs` contains pairs `(query_value,original_index)` sorted by value. The algorithm processes thresholds from smallest to largest while `ans` remains indexed in the original order.

After finishing threshold `v`, it writes the current reachable count into `ans[k]`. Equal query values naturally receive the same count because no new cell can be popped between identical thresholds after the first has exhausted all values below that threshold.

**Maintain the smallest boundary cell in a heap**

The min-heap `q` begins with the top-left cell represented as `(grid[0][0],0,0)`. It contains discovered cells adjacent to the already expanded region that have not yet been counted.

For a query value `v`, the loop pops while the smallest heap value is strictly less than `v`. A popped cell is eligible for this query, so `cnt` increases. Its four neighbors are then discovered and pushed if they have never been seen.

If the smallest boundary value is at least `v`, no heap cell is eligible. Because it is the minimum, every other boundary cell is also too large. Any route to an undiscovered cell must cross the current boundary, so expansion cannot legally proceed for this threshold.

**Why a popped cell is truly reachable**

The start cell is the initial frontier. Every later cell enters the heap only when an already popped cell reveals it. Thus it has a chain of predecessor cells back to `(0,0)`.

When it is finally popped for threshold `v`, its own value is below `v`. Every predecessor was popped under the same or an earlier, no-larger sorted threshold, so every predecessor value is also below `v`. The chain is a valid path for the current query.

Therefore, incrementing `cnt` never counts an unreachable cell.

**Why every reachable cell is eventually popped**

Take any cell reachable under threshold `v` and consider a valid path from the start to it. The start is placed in the heap initially. Whenever a path cell is popped, the next path cell is marked and pushed. Since every cell on the path has value below `v`, it cannot remain behind a heap minimum of value at least `v`. Repeated popping eventually reaches the target.

Hence, after the inner loop stops, `cnt` equals exactly the maximum number of points for that query.

**Mark cells when pushing, not when popping**

`vis[x][y]` becomes true immediately before a neighbor is pushed. A grid cell can border several popped cells; early marking prevents duplicate heap entries and duplicate counting.

This is safe even if the new cell is too large for the current query. It remains in the heap as a boundary candidate for a later larger threshold. Discovering it through another path would not lower its fixed cell value or make it a different cell.

Each cell is therefore pushed and popped at most once.

**Strict inequality matters**

The heap condition is `q[0][0] < v`, not `<=v`. A query must be strictly greater than the current cell's value. A cell whose value equals the query blocks movement and awards no point.

If `grid[0][0]>=v`, even the start cannot be counted. It remains at the heap top, the loop performs no expansion, and the answer is zero.

**Four directions**

`pairwise((-1,0,1,0,-1))` yields direction pairs

`(-1,0)`, `(0,1)`, `(1,0)`, and `(0,-1)`.

These correspond to up, right, down, and left. Bounds checks exclude coordinates outside the matrix.

**Incremental state across queries**

The heap, visited matrix, and `cnt` are intentionally not reset. When the threshold increases, all previously popped cells remain valid and counted. The heap retains precisely the not-yet-eligible boundary accumulated so far.

This reuse is the central optimization. Running a fresh search for every one of up to $10^4$ queries would repeat the same grid work many times.

## Complexity detail

Let $N=mn$ be the number of grid cells and $k$ the number of queries. Sorting queries costs $O(k\log k)$.

Each cell is pushed into and popped from the heap at most once. A heap operation costs $O(\log N)$, and each pop examines four neighbors, so total grid expansion costs $O(N\log N)$. Overall time is

$$
O(N\log N+k\log k).
$$

The heap and visited matrix can each hold $O(N)$ data. Sorted query pairs and the answer use $O(k)$. Total auxiliary space is $O(N+k)$.

## Alternatives and edge cases

- **Fresh BFS per query:** It is correct but can cost $O(kmn)$ and repeats reachability work.
- **Union-find offline:** Sort cells by value, activate them below each sorted query, and track the component containing the start. It has comparable offline efficiency.
- **Equal cell and query values:** The cell is not eligible because the comparison is strict.
- **Blocked start:** The answer is zero and no neighbors can be reached.
- **Duplicate queries:** They receive identical counts and retain their separate original positions.
- **Unsorted input queries:** Sorting enables reuse; `original_index` restores output order.
- **Cell discovered early but too large:** Leave it in the heap for a later threshold.
- **Multiple paths to one cell:** Marking on push prevents duplicates.
- **Revisiting allowed:** It cannot earn another point, so visited-state counting remains correct.
- **Heap frontier:** If its minimum is blocked, every route to undiscovered cells is blocked for that threshold.
