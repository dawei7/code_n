## General

**Reverse the direction of the search**

A direct interpretation would start from each empty room and search outward until finding a gate. That repeats much of the same grid exploration for many rooms. The optimal insight is to reverse the perspective: start from every gate simultaneously and let distance waves spread into empty rooms.

This is multi-source breadth-first search. Ordinary BFS from one source reaches positions in nondecreasing distance from that source. Placing all gates in the initial queue is equivalent to adding an imaginary super-source connected to every gate by a zero-cost setup: the first wave reaches rooms one step from any gate, the second reaches rooms two steps from their nearest gate, and so on.

Because the waves compete in one shared queue, a room is claimed by whichever gate can reach it at the smallest distance. No separate comparison among gates is needed.

**Interpret the three grid values as both data and state**

The grid begins with:

- `0` for a gate;
- `-1` for a wall; and
- `2**31 - 1` for an unfilled empty room.

The source stores the infinity sentinel in `inf`. During BFS, an `inf` cell means both “this is traversable empty space” and “this room has not yet been visited.” As soon as the algorithm assigns a finite distance, the cell becomes its own visited marker.

This reuse avoids a separate `visited` matrix. Gates and walls are never confused with unvisited rooms because neither equals `inf`.

**Seed the queue with every gate**

The queue comprehension scans all `m * n` cells and inserts the coordinates of every cell whose value is zero. All gates therefore occupy BFS layer zero before expansion begins.

Starting from all gates at once is essential. If gates were processed with separate BFS runs that overwrote rooms, later searches would need comparisons and could revisit the entire grid. In the shared queue, the standard BFS ordering resolves the minimum distance automatically.

If there are no gates, the queue is empty. The BFS loop never runs, and every empty room correctly remains `INF` because no gate is reachable anywhere.

**Process one complete distance layer at a time**

The variable `d` begins at zero. At the start of each outer iteration, the source increments it. The coordinates currently in the queue are exactly the cells at distance `d - 1` from their nearest gate. Their newly discovered neighbors must therefore receive distance `d`.

The loop `for _ in range(len(q))` captures the current layer's queue size before processing it. Newly discovered rooms are appended to the queue, but they are not processed until the next outer iteration. This separation is what makes one shared scalar `d` correct for every room in a layer.

On the first iteration, the queue contains gates at distance zero, `d` becomes one, and neighboring rooms receive one. On the next iteration, those distance-one rooms expand and assign two, continuing outward.

**Explore only legal orthogonal neighbors**

From each dequeued cell `(i, j)`, the algorithm considers four offsets: right, left, down, and up. Diagonal movement is excluded because the distance contract counts only horizontal or vertical steps.

For neighbor `(x, y)`, three conditions must hold:

1. `x` lies from 0 through `m - 1`;
2. `y` lies from 0 through `n - 1`; and
3. `rooms[x][y] == inf`.

The bounds prevent invalid indexing. The infinity check simultaneously excludes walls, gates, and rooms already assigned a distance. When all conditions hold, the source writes `d` into the room and appends its coordinates for the next layer.

**Why assignment happens when enqueuing**

A room can border several cells in the same or different BFS layers. If it were marked only when later dequeued, several parents could enqueue it repeatedly. Writing its distance immediately makes every later attempt see a non-`inf` value and skip it.

The first attempt is guaranteed to carry the shortest possible distance because BFS processes all smaller-distance layers before larger ones. Other gates or paths may reach the room with the same distance, but the value would be identical, so retaining only the first discovery is sufficient.

**Why the first assigned value is the nearest-gate distance**

Consider any empty room first discovered in layer $d$. The queue path that discovered it gives an actual route of exactly $d$ orthogonal steps from some gate, so its nearest-gate distance is at most $d$.

If a shorter route of length less than $d$ existed, that route would begin at one of the gates already in layer zero. BFS would have followed its successive cells through earlier layers and discovered the room before layer $d$. That contradicts this being the first discovery. Therefore, no shorter route exists and the assigned value equals the nearest distance.

Walls cannot appear along a discovery path because only `inf` rooms are enqueued after the initial gates. A room separated from every gate by walls is never discovered and retains `INF`, exactly as required.

**A layer invariant**

Before each outer iteration with current `d`, every finite non-gate distance already written is correct, and the queue contains exactly the discovered cells at the previous distance layer that have not yet expanded. Processing the fixed queue snapshot assigns the next distance only to previously unvisited rooms. The shortest-path argument proves those assignments correct, and appending them establishes the queue for the next layer.

When the queue becomes empty, every room reachable from any gate has been assigned. Any remaining `INF` room has no traversable path to a gate, because otherwise the search would eventually have followed that finite path to it.

**Trace the beginning of the main example**

The input has gates at the top row's third cell and the bottom row's first cell. Both enter the initial queue with grid value zero.

At `d = 1`, all accessible neighbors of either gate are filled with 1. At `d = 2`, the newly filled distance-one rooms expand together, claiming previously untouched neighbors. If wave fronts from the two gates approach the same area, the room is assigned by the first layer that reaches it; because both fronts use the same global layers, that is the minimum distance.

Walls remain `-1`, gate values remain zero, and the final grid contains distances such as 3, 2, 1, and 0 along shortest routes. The isolated wall-only example `[[-1]]` seeds no gate, performs no writes, and remains unchanged.

## Complexity detail

Let the grid have $m$ rows and $n$ columns. The initial comprehension scans all $mn$ cells. Each gate is enqueued once initially, and each reachable empty room is enqueued once when its value changes from `INF` to a finite distance. Walls and already visited cells are never enqueued.

Every dequeued coordinate examines exactly four directions, so total BFS work is $O(mn)$. Including initialization, time complexity is $O(mn)$.

In the worst case, the queue can hold $O(mn)$ coordinates in a wide BFS frontier or when many cells are gates. Auxiliary space is therefore $O(mn)$. The algorithm modifies the grid in place and does not allocate a second distance matrix.

The direction list created inside the loop has four constant-size pairs, so it does not change the asymptotic space bound. A module-level tuple of directions could avoid recreating this small object for each popped cell.

## Alternatives and edge cases

- **BFS from every empty room:** It can find a nearest gate but repeats exploration and costs up to $O(m^2n^2)$ time.
- **Separate BFS from every gate:** Distances must be minimized across runs, and cells may be revisited many times. Multi-source BFS combines all gates into one shortest-path computation.
- **DFS from gates:** DFS does not process paths by increasing length. It needs repeated relaxation or careful pruning to correct distances, while BFS provides shortest unweighted paths directly.
- **No gates:** The initial queue is empty and all empty rooms remain `INF`.
- **No empty rooms:** Gates and walls seed or skip normally, but no neighbor ever passes the `inf` test, so the grid is unchanged.
- **Room enclosed by walls:** It is never enqueued and correctly remains `INF`.
- **Multiple equally near gates:** The first discovery assigns the shared minimum distance. The identity of the winning gate is irrelevant.
- **Adjacent gate:** An empty room sharing an edge with any gate is assigned 1 in the first layer.
- **Walls:** Their `-1` value fails the infinity test, so search never crosses or modifies them.
- **Gates:** Their zero value also fails the infinity test after initialization, preventing one gate's wave from overwriting another gate.
- **One-cell wall grid:** No gate is enqueued and no mutation occurs, matching the second example.
- **One-cell gate grid:** The gate is processed, has no in-bounds neighbors, and stays zero.
- **Rectangular rather than square grids:** Separate `m` and `n` bounds handle all legal dimensions.
- **In-place contract:** Finite distances double as visited markers. Replacing them later with larger values would break the one-visit proof; the BFS first-arrival guarantee makes replacement unnecessary.
