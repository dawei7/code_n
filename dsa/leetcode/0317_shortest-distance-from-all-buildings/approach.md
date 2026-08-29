## General

The desired house must be placed on an empty cell and must be reachable from every building. Obstacles and buildings cannot be crossed, so Manhattan distance alone is insufficient: a geometrically nearby building may require a detour or may be unreachable.

Because every legal move has equal cost one, breadth-first search finds shortest grid-path distances. The source runs one BFS from each building. Whenever that BFS reaches an empty cell, it adds the building-to-cell distance to a cumulative total and increments the number of buildings that reached the cell.

After all building searches, an empty cell is eligible only when its reach count equals the total number of buildings. Among eligible cells, the smallest accumulated distance is the answer.

**Why searching from buildings is equivalent**

Legal movement between empty cells is undirected. If an empty cell can reach a building along a path of passable empty cells ending beside that building, the same path can be followed in reverse from the building to the empty cell.

Therefore, instead of starting one search from every candidate land cell, the algorithm can start from each building and distribute that building's distance to all reachable candidates. Summing those contributions later gives the same total distance for each land cell.

**The two accumulation matrices**

`cnt[r][c]` is the number of processed building searches that reached empty cell `(r, c)`.

`dist[r][c]` is the sum of the shortest distances from those buildings to that cell.

These meanings must be kept separate. A small distance sum is irrelevant if only some buildings can reach the cell. The count matrix proves universal reachability; the distance matrix provides the objective value once reachability is established.

Both matrices start at zero. Buildings and obstacles never need meaningful entries because the final house candidate must have original grid value zero.

**Starting one building BFS**

When the outer grid scan finds `grid[i][j] == 1`, it increments `total`, places `(i, j)` in the queue, resets level distance `d = 0`, and creates a fresh visited set `vis`.

The visited set is local to one building. An empty cell should be counted once for each different building, so visitation information must not carry across searches. Within one search, however, a cell may be reachable by several paths and must be accumulated only once at its shortest distance.

The queue object is created before the outer scan but is empty after every completed BFS. Each building appends its start only after the previous search has drained the queue, so searches remain independent.

**Why queue layers equal shortest distance**

At the start of a `while q` round, all queued cells are at one common distance from the source building. The source increments `d`, snapshots `len(q)`, and expands exactly those current-layer cells.

The initial queue contains the building itself. The first round sets `d = 1`, so adjacent empty cells receive distance one. Those cells are appended behind the current layer and are processed in the next round, where their newly discovered neighbors receive distance two.

Because BFS explores all paths of length $d$ before paths of length $d+1$, the first time an empty cell is discovered is through a shortest path. No later route can improve its distance.

**Enqueue-time visitation**

A neighbor `(x, y)` is accepted only when:

- its row and column are inside the grid;
- `grid[x][y] == 0`, so it is traversable empty land;
- it is not already in this building's `vis` set.

As soon as the cell is accepted, the source updates its count and distance, appends it to the queue, and adds it to `vis`.

Marking at enqueue time is essential. If marking waited until dequeue, two cells in the same layer could both enqueue the same neighbor, causing duplicate distance addition and inflated reach count.

The source does not put the starting building in `vis`, but this causes no issue because only grid-zero neighbors can ever be enqueued. Buildings have value 1 and cannot be revisited or used as transit cells.

**Why buildings are not traversed through**

The neighbor condition accepts only zeros. Obstacles with value 2 and all buildings with value 1 block expansion. This matches the contract: a route may pass freely through empty land, but cannot pass through a building or obstacle.

The source building is present only as the initial queue seed. BFS steps outward from it to adjacent empty cells; another building encountered later is neither accumulated as a candidate nor crossed.

**Accumulating one contribution**

When a cell is first reached at level `d`, the source performs

`cnt[x][y] += 1`

and

`dist[x][y] += d`.

The first operation records that this particular building can reach the cell. The second adds that building's shortest distance. Since one BFS visits a cell at most once, it contributes exactly one count and one shortest-distance term.

After all $b$ buildings have been processed, a cell with `cnt == b` has cumulative value

$$
\sum_{t=1}^{b}\operatorname{distance}(building_t,cell).
$$

**Tracing the sample conceptually**

In the first example, BFS runs from buildings `(0,0)`, `(0,4)`, and `(2,2)`. Empty cell `(1,2)` is reachable from all three.

Its shortest distances are 3, 3, and 1, so its count becomes three and its accumulated distance becomes

$$
3+3+1=7.
$$

The obstacle at `(0,2)` is never enqueued, so paths correctly route around it. After every building search, the final scan compares `(1,2)` with every other empty cell whose count is also three and finds seven to be minimal.

**Selecting the final answer**

`ans` begins at positive infinity. The final double loop considers only cells satisfying both:

- `grid[i][j] == 0`;
- `cnt[i][j] == total`.

The first ensures a house can legally be built there. The second ensures every building reaches it. The source minimizes `dist[i][j]` among exactly those candidates.

If no eligible cell exists, `ans` remains infinity and the method returns `-1`. This covers disconnected empty regions, grids with no empty cell, and any arrangement where no single land cell is reachable from all buildings.

**Why the result is correct**

For each building, BFS assigns every reachable empty cell its exact shortest distance and leaves unreachable cells unchanged. Inductively, after processing some buildings, `cnt` records exactly how many reached each cell and `dist` is exactly the sum of their shortest distances.

After all searches, count equality with `total` is equivalent to reachability from every building. The final minimum therefore ranges over all and only legal house positions and compares their exact total travel distances. Its returned finite value is optimal, while absence of a candidate correctly yields `-1`.

## Complexity detail

Let $m$ be the row count, $n$ the column count, and $b$ the number of buildings.

One building BFS can visit at most all $mn$ cells and inspect four neighbors per visited cell, costing $O(mn)$ time. Running it for every building costs $O(bmn)$. The initial and final grid scans add $O(mn)$, which is dominated when $b\ge1$.

The `cnt` and `dist` matrices each use $O(mn)$ space. During one BFS, the visited set and queue can also hold $O(mn)$ coordinates. Searches reuse that working memory rather than retaining one set per building, so total auxiliary space is $O(mn)$.

The returned result is one integer. The source's complexity matches the manifest; it does not implement the editorial's cross-building reachability pruning, though both share the same stated worst-case class.

## Alternatives and edge cases

- **Grid-marker pruning between building searches:** After each BFS, mutate reachable zeros to the next marker and let the next building traverse only cells reached by all prior buildings. This can prune impossible regions and avoid a fresh visited matrix, but the exact source uses independent sets.
- **BFS from every empty land:** Sum distances to buildings from each candidate. It is correct but can be much slower when empty cells greatly outnumber buildings.
- **Manhattan distance:** It ignores obstacles and impassable buildings, so it can underestimate or claim a route where none exists.
- **Multi-source BFS from all buildings at once:** It finds distance to the nearest building, not the sum of separate shortest distances to every building.
- **DFS:** It can discover reachability but does not naturally guarantee shortest paths in an unweighted graph without additional distance relaxation.
- **Reuse one visited set across buildings:** This would prevent later buildings from contributing to cells already visited by earlier searches.
- **Mark at dequeue time:** The same cell may enter the queue multiple times from one level, corrupting counts and sums.
- **Allow traversal through a building:** The rules make buildings impassable, so another building cannot serve as a corridor.
- **One building and adjacent land:** That land receives count one and distance one, yielding answer one if no closer legal cell exists.
- **Only a building:** There is no empty candidate; infinity remains and the answer is `-1`.
- **Unreachable region:** Its cells have reach count below `total` and are excluded regardless of their partial distance sum.
- **Several equal optima:** The problem asks only for the minimum distance, so no coordinate tie handling is needed.
- **Obstacles enclosing a building:** If that prevents every empty cell from reaching all buildings, no count reaches `total` and the method returns `-1`.
- **Boundary cells:** Explicit range tests prevent grid wrapping and out-of-bounds access.
- **At least one building:** `total` is positive, so a never-reached empty cell with count zero cannot accidentally qualify.
