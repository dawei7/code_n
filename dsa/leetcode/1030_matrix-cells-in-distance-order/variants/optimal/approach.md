## General

**Manhattan distance is shortest-path distance in this grid**

Treat every matrix cell as a vertex. Connect two vertices when their cells share an edge. Every move changes the row by one or the column by one, so each edge has unit cost.

To travel from `(rCenter, cCenter)` to `(r, c)`, any path must make at least `|r - rCenter|` vertical moves and `|c - cCenter|` horizontal moves. A path that makes exactly those moves exists inside the rectangular matrix: move toward the target row, then toward the target column. Its length is

$$
\lvert r-rCenter\rvert+\lvert c-cCenter\rvert.
$$

Therefore, the required Manhattan distance is exactly the unweighted graph distance from the center. Breadth-first search visits an unweighted graph in nondecreasing shortest-path distance, so its visitation order is already a valid answer order. No comparison sort is needed.

**Initialize distance zero**

The queue begins with `[rCenter, cCenter]`. The center is the unique cell at distance zero, so it must appear first.

The Boolean matrix `vis` records whether a cell has already been discovered. The center is marked immediately. Marking on enqueue, rather than waiting until dequeue, ensures that two neighboring cells cannot add the same coordinate twice.

The answer starts empty. A coordinate is appended when removed from the front of the queue, which is when BFS processes it in distance order.

**Why the outer loop is divided into layers**

At the start of each `while q` iteration, all cells currently in the queue belong to one distance layer. The expression `range(len(q))` snapshots how many such cells exist.

New neighbors discovered during that loop are appended to the back of the queue. They are one move farther away and are not included in the already-created `range`, so they wait until the next outer iteration.

Consequently, the algorithm appends all distance-zero cells, then all distance-one cells, then all distance-two cells, and so forth. The problem permits any order among cells with equal distance, so the precise order within a layer is irrelevant.

A standard FIFO BFS would preserve the same order even without the explicit layer loop. The loop makes the distance grouping visible and prevents any doubt that newly discovered cells are processed only after the current layer.

**Generate the four legal neighbors**

The tuple `(-1, 0, 1, 0, -1)` compactly encodes direction changes. Applying `pairwise` yields:

- `(-1, 0)` for up.
- `(0, 1)` for right.
- `(1, 0)` for down.
- `(0, -1)` for left.

For a processed coordinate `p`, the candidate neighbor is `(x, y) = (p[0] + a, p[1] + b)`.

The condition `0 <= x < rows and 0 <= y < cols` keeps the candidate inside the matrix. Python short-circuits the conjunction, so `vis[x][y]` is checked only after bounds are proven. If the cell has not been visited, it is marked and appended to the queue.

Diagonal neighbors are intentionally absent. A diagonal displacement changes both row and column and would count as two units of Manhattan distance, not one.

**Trace a small matrix**

Take a `2 \times 3` matrix with center `(1, 2)`.

The first layer contains only `[1, 2]` and appends it at distance zero. Its valid unvisited neighbors are `[0, 2]` and `[1, 1]`, both at distance one.

The second layer processes those two cells. They discover `[0, 1]` and `[1, 0]` at distance two. A cell reachable from both is enqueued only by the first discovery because `vis` is already true on the second attempt.

The next layer processes the distance-two cells and eventually discovers `[0, 0]` at distance three. The resulting order may differ within a layer depending on direction order, but the distances are `0, 1, 1, 2, 2, 3` as required.

**Why every cell is reached**

The rectangular grid graph is connected. From the center, repeatedly changing the row toward any target and then changing the column reaches that target without leaving the matrix. BFS explores every reachable neighbor, so eventually every one of the `rows * cols` coordinates is discovered.

The visited matrix prevents duplicates, so every coordinate is appended exactly once. The answer therefore has exactly the required number of entries and contains no coordinate outside the matrix.

**Why the order is correct**

BFS begins at distance zero. Whenever it processes a cell at distance `d`, each newly discovered neighbor has a path of length `d + 1`. If that neighbor had a shorter path, BFS would have discovered it in an earlier layer. Thus first discovery assigns its true shortest-path distance.

The layer queue ensures no distance-`d + 1` cell is dequeued before all distance-`d` cells. Since shortest-path distance equals Manhattan distance here, the appended coordinates are nondecreasing by the exact metric in the question.

**Why a visited matrix is still necessary in an obstacle-free grid**

Most cells have several paths from the center. Without `vis`, a cell could be enqueued once from its upper neighbor and again from its left neighbor, causing duplicates and an explosive amount of repeated work. Discovery marking chooses one shortest path and discards all redundant arrivals.

The matrix contains no blocked cells, but multiple paths alone are enough to require duplicate prevention.

## Complexity detail

Let `M = rows \cdot cols` be the number of cells. Every cell is enqueued once, dequeued once, appended once, and checks four neighbors. The constant factor of four does not change the bound, so time complexity is `O(M)`, matching the manifest.

The visited matrix uses `O(M)` Boolean entries. The queue can contain `O(M)` cells in a broad distance layer in the general bound, and the returned answer contains all `M` coordinates. Total space is `O(M)`. If required output is excluded, the visited matrix and queue still give an `O(M)` auxiliary bound.

This running time is optimal because the required output itself contains `M` coordinate pairs; any solution must spend at least `\Omega(M)` time producing them.

## Alternatives and edge cases

- **Generate all cells and comparison-sort:** Compute each Manhattan distance and sort coordinates by it. This is simple but costs `O(M \log M)` time instead of exploiting bounded integer distance layers.
- **Bucket by distance:** The maximum possible distance is at most `rows + cols - 2`. Append every cell to its distance bucket and concatenate buckets. This also runs in `O(M + rows + cols)` time but requires explicit buckets.
- **Direct diamond-ring generation:** Enumerate coordinates at distance zero, one, two, and so on around the center. It can use little visited state, but handling clipped diamonds at matrix borders without duplicates is more error-prone.
- **Priority queue:** Push cells keyed by distance. It produces sorted order but adds `O(\log M)` overhead to each extraction even though BFS already supplies the correct layers.
- **One cell:** The queue contains only the center, which is appended and returned.
- **One row:** BFS expands left and right along a line, still producing nondecreasing absolute column distance.
- **One column:** The same reasoning applies vertically.
- **Center on a corner:** Every cell lies in directions inward from the corner; invalid outward neighbors are rejected by bounds checks.
- **Center in the interior:** Several cells share each distance. Any of their relative orders is accepted.
- **Duplicate discovery paths:** Marking at enqueue time prevents a coordinate from entering the queue more than once.
- **Tie ordering:** The up, right, down, left direction order determines one valid order among equal-distance cells, but correctness does not depend on that choice.
- **No obstacles:** Manhattan distance equals graph distance because every monotone row-and-column path stays within the rectangle. With obstacles, BFS distance could be larger and the problem would be different.
- **Imports supplied by the environment:** The exact solution uses `deque` and `pairwise`. They must be available from the solution environment, but they do not change the algorithmic reasoning.
