## General

**Reverse the viewpoint: expand from every land cell**

For each water cell, the desired value is its distance to the nearest land cell. Running a separate breadth-first search from every water cell would repeat most of the same exploration.

Instead, place all land cells into one queue before the search begins. This is multi-source breadth-first search. It behaves as if a new virtual source were connected to every land cell with zero-cost edges. The first search wave reaches all water cells at distance one, the next reaches distance two, and so on.

Because the final wave contains the water cells with the greatest nearest-land distance, the number of completed waves gives the answer.

**Initialize every distance-zero source**

The deque comprehension scans all `n^2` coordinates and inserts `(i, j)` whenever `grid[i][j]` is one. These are exactly the land cells, and each has distance zero from the nearest land because it is land itself.

The early condition handles the two invalid result cases:

- an empty queue means there is no land, so no water cell has a finite distance to land;
- a queue of size `n * n` means every cell is land, so there is no water cell to choose.

Both return the initial `ans = -1` as required.

**Process one distance layer at a time**

At the beginning of a `while q` iteration, the queue contains all cells at one BFS distance layer. `range(len(q))` captures that layer's size before any new cells are appended.

Every current cell explores its four orthogonal neighbors. The compact direction tuple

`(-1, 0, 1, 0, -1)`

combined with `pairwise` produces the offsets up `(-1, 0)`, right `(0, 1)`, down `(1, 0)`, and left `(0, -1)`. These are exactly the moves whose shortest-path length equals Manhattan distance.

A neighbor is accepted only when it lies inside the grid and its current value is zero. The solution immediately changes it to one and appends it.

Changing the grid at discovery time is the visited marker. Immediate marking is important: if two cells in the current frontier can both reach the same water cell, the first one marks it before the second examines it, so the cell enters the queue only once.

**Understand the distance counter**

`ans` begins at negative one. After processing the initial land layer, it is incremented to zero. Those source cells have distance zero.

The next queue layer contains water cells one step from land. After processing that layer, `ans` becomes one. The pattern continues: after the layer of distance `d` is processed, `ans == d`.

When the queue becomes empty, the last processed layer is the greatest distance reached. Because both all-land and no-land inputs were removed earlier, at least one water layer exists, and the returned value is the maximum nearest-land distance.

**Why the first visit gives the nearest land**

Breadth-first search explores unweighted graph edges in nondecreasing path length. With all land sources present at level zero, a water cell discovered at level `d` has a path of length `d` to some land source.

If it had a shorter path to any land, the search wave from that source would have reached it in an earlier layer. Since the cell was still unvisited, no such shorter path exists. Its discovery level is therefore exactly its Manhattan distance to the nearest land.

The last discovered distance is the maximum of these exact nearest-land distances over all water cells, which is precisely the requested quantity.

**Trace the corner-land example**

If only `(0, 0)` is land in a three-by-three grid, the initial queue contains that source. Distance-one cells are `(0, 1)` and `(1, 0)`. Later waves reach cells whose coordinate sum is two, then three, and finally `(2, 2)` at distance four. The final counter is four.

**Why the input is modified**

The algorithm reuses zero and one as unvisited-water and visited-or-land states. This avoids allocating a separate `n` by `n` visited matrix. After execution, every reachable water cell has been changed to one, so callers should not expect the original grid contents to remain intact.

Under this problem's one-shot method contract, mutation is safe because the grid is not needed after the distance is returned.

## Complexity detail

There are `n^2` cells. Initial source collection scans all of them once. Each water cell is marked and enqueued at most once, and each dequeued cell examines exactly four neighbors. Total time is `O(n^2)`.

The queue may hold `O(n^2)` coordinates in a broad frontier, including the initial all-land-like source set before the early check. The auxiliary space complexity is `O(n^2)`.

No separate visited matrix is allocated because the input grid is used for marking. The coordinate tuples in the queue account for the stated bound.

## Alternatives and edge cases

- **BFS from every water cell:** This repeats searches and can take `O(n^4)` time on an `n` by `n` grid.
- **Dynamic programming in directional passes:** Distances can be propagated with forward and backward scans in `O(n^2)` time. Multi-source BFS more directly matches unweighted Manhattan layers.
- **Use a separate visited set:** It preserves the input but adds another `O(n^2)` structure. The exact solution intentionally marks the grid.
- **Mark cells when dequeued:** Several parents could enqueue the same water cell before its first dequeue. Marking at discovery prevents duplicates.
- **No land:** The initial queue is empty and the answer is `-1` because nearest-land distance is undefined.
- **No water:** Every cell is already in the source queue and the answer is `-1` because there is no candidate water cell.
- **One land cell:** BFS radiates from that source, and the farthest grid position determines the result.
- **Several land cells:** Their waves run simultaneously; the first wave to reach a water cell automatically represents its nearest source.
- **One-cell grid:** It is either all land or all water, so the early condition returns `-1`.
- **Input mutation:** Every visited water cell becomes one. A caller needing the original grid would have to pass a copy, adding `O(n^2)` space.
- **Only orthogonal movement:** Diagonal steps are not explored because Manhattan distance counts horizontal and vertical moves only.
