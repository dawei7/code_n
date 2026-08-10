## General

**Separate discovery from shortest-path search**

The robot cannot inspect the hidden grid directly. It can only ask whether a move is possible, physically move, and test its current cell for the target.

The exact solution uses two phases:

- A depth-first traversal controls the robot, assigns relative coordinates to reachable cells, and backtracks after every exploration.
- A breadth-first search runs on the discovered coordinate set to compute the true shortest number of moves from start to target.

DFS is convenient for physically exploring and restoring position. BFS is necessary afterward because the order in which DFS first reaches the target does not guarantee a shortest path.

**Invent coordinates relative to the unknown start**

The start is labeled coordinate `(0, 0)`. These coordinates do not need to match the hidden grid's real row and column numbers. They only need to preserve relative moves.

Direction string `s = "URDL"` pairs with:

`dirs = (-1, 0, 1, 0, -1)`.

For direction index `k`, delta is `(dirs[k], dirs[k + 1])`:

- U gives minus one, zero.
- R gives zero, one.
- D gives one, zero.
- L gives zero, minus one.

Moving the robot and applying the same delta keeps the invented coordinate consistent with physical location.

**Explore a legal unvisited neighbor**

At coordinate `(i, j)`, DFS considers every direction character `c`. It first asks `master.canMove(c)`. It also requires that the corresponding coordinate `(x, y)` is not already in `vis`.

When both conditions hold, it:

- adds the coordinate to `vis`,
- physically calls `master.move(c)`,
- recursively explores from `(x, y)`,
- physically moves in the opposite direction to return.

The opposite direction is `s[(k + 2) % 4]`: up pairs with down, and right pairs with left. This final move restores the robot to `(i, j)`, so the next loop direction is tested from the correct physical cell.

**Record the target in relative coordinates**

At entry to DFS, `master.isTarget()` tests the robot's current physical cell. If true, `target` is set to the current invented coordinate and that recursive call returns.

The DFS does not explore through the target. Cells reachable only beyond it are unnecessary for finding a path to the target: reaching the target already completes any such route. The recursive caller still executes its opposite move, returning the robot correctly.

If exploration finishes with `target is None`, no reachable cell was the target and the method returns minus one before BFS.

**Understand the start-cell visitation detail**

`vis` begins empty rather than containing `(0, 0)`. Consequently, during DFS from a non-target neighbor, the edge back to the start may cause the start coordinate to be added and explored once as if newly discovered.

This can create one redundant recursive visit, but it does not make exploration infinite: after insertion, `(0, 0)` is in `vis` and cannot be added again. Other discovered coordinates are also protected by the set.

Before BFS, `vis.discard((0, 0))` removes the start if that rediscovery occurred. `discard` is safe even if the start was never inserted. The BFS queue itself already represents the start.

**Backtracking keeps the interactive state synchronized**

The coordinate variables alone do not move the actual robot. Every recursive descent must call `master.move(c)`, and every return must issue the inverse move.

Because the grid is undirected for movement, a direction accepted on descent has a valid opposite on immediate backtracking. This maintains the invariant that entering `dfs(i, j)` means the robot physically occupies the cell represented by `(i, j)`.

Without backtracking, later `canMove` calls would be asked from a different cell than the coordinates claim, corrupting the map.

**Run BFS over discovered open cells**

Once the target coordinate is known, the physical master is no longer needed. `vis` serves as the set of open, reachable, unvisited coordinates.

The source initializes `q` with start and `ans = -1`. At the beginning of each BFS layer, it increments `ans`. Therefore the start layer has distance zero.

For each dequeued coordinate, it first checks equality with `target`. Then it examines the four coordinate neighbors using `pairwise(dirs)`. A neighbor present in `vis` is removed immediately and enqueued.

Removing on enqueue marks it visited, preventing duplicate queue entries. BFS layers guarantee that the first dequeue of a coordinate uses the fewest grid moves from start.

**Why the two-phase result is correct**

The backtracking DFS discovers every reachable open coordinate needed to reach the target and records the target's relative position. It never records a blocked cell because movement is attempted only after `canMove` succeeds.

BFS traverses the unweighted adjacency graph of those coordinates. In an unweighted graph, BFS's first target layer is the shortest path length. If the target was unreachable, the earlier null check returns minus one. Thus the final returned distance matches the hidden grid.

## Complexity detail

Let $V$ be the number of reachable open cells discovered and $E$ their grid adjacencies. A grid has at most four edges per cell, so $E=O(V)$.

DFS visits each coordinate at most once apart from the possible one redundant start visit, tests four directions, and physically traverses exploration edges forward and backward. BFS visits each discovered coordinate once. Total time and interactive query work are $O(V)$.

`vis`, the BFS deque, and recursive DFS stack can each hold $O(V)$ coordinates in the worst case. Total space is $O(V)$, matching the manifest.

For a very deep hidden corridor, recursive DFS depth can approach $V$ and may exceed Python's default recursion limit even though the algorithmic bound is correct.

## Alternatives and edge cases

- **BFS directly through GridMaster:** A queue cannot freely jump the physical robot between frontier cells, so interactive movement and restoration become difficult.
- **DFS distance only:** The first target discovery is not necessarily the shortest path.
- **Build an explicit adjacency map:** It is unnecessary because discovered coordinates and four-direction geometry determine adjacency.
- **Target adjacent to start:** DFS records it, and BFS returns one.
- **Target unreachable:** DFS never sets `target` and the method returns minus one.
- **Start differs from target:** The guarantee makes the initial target check false.
- **Blocked direction:** `canMove` prevents both coordinate insertion and physical movement.
- **Target early return:** Its neighbors are not explored, but no path needs to continue beyond the destination.
- **Opposite direction:** Adding two modulo four maps U to D and R to L.
- **Start not initially visited:** It may be rediscovered once; `discard` normalizes the BFS set.
- **Multiple routes to one cell:** `vis` ensures one DFS discovery, while BFS later finds the shortest route.
- **BFS mark on enqueue:** Removing from `vis` prevents duplicate frontier entries.
- **Relative coordinates:** Absolute hidden-grid dimensions and start location are never needed.
- **Recursion depth:** A long corridor is a practical Python stack risk.
- **Master position after DFS:** Balanced descent and opposite moves restore it to the start.
