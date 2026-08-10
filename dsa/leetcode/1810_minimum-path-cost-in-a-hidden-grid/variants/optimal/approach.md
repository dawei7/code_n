## General

**Separate discovery from shortest-path optimization**

The robot knows the grid only through `GridMaster` and physically changes position when `move` is called. A shortest-path algorithm cannot run until reachable cells and their entry costs are known.

The protected solution therefore has two phases:

1. depth-first exploration controls the robot, maps every reachable cell into local coordinates, and records the target;
2. Dijkstra's algorithm runs on that discovered weighted map without further interactive movement.

This separation prevents shortest-path bookkeeping from becoming entangled with the robot's physical location.

**Create a safe local coordinate system**

The real grid has at most 100 rows and 100 columns, but its dimensions and start coordinates are hidden. The solution allocates a 200 by 200 array `g` and places the unknown start at synthetic coordinate `(100,100)`.

Any real reachable cell differs from the start by at most 99 rows and 99 columns, so its translated coordinate fits in the allocated range.

Value -1 means not yet discovered. A discovered cell stores the cost returned when the robot moves into it.

**Explore with reversible DFS movement**

Directions `"URDL"` correspond to coordinate steps from `dirs = (-1,0,1,0,-1)`. For direction index $k$, `dirs[k]` and `dirs[k+1]` form its row and column change.

At DFS coordinate `(x,y)`, `master.isTarget()` records that coordinate when true. Then each direction is considered.

A neighbor is explored only when it stays inside the synthetic array, still has `g[nx][ny] == -1`, and `master.canMove(direction)` reports that movement is legal. The forward `move` returns the destination's entry cost, which is stored before recursion.

After the recursive call finishes, the robot must return to the caller's physical cell. Direction index `(k + 2) % 4` is the opposite direction, so a second `move` backtracks. The return cost is irrelevant to mapping because the earlier cell is already known.

This restoration is the DFS invariant: whenever `dfs(x,y)` begins and ends, the robot is physically at the cell represented by `(x,y)`.

**The exact start-cell marking behavior**

The source initially leaves `g[100][100]` at -1. After the first move to a neighbor, that neighbor's DFS can see the start as an unvisited reachable neighbor, move back into it, record the start cell's entry cost, and recurse once from it. The path is then marked, so this does not repeat indefinitely.

This causes one redundant rediscovery of the synthetic start whenever a reachable neighbor exists, but correctness remains intact under the undirected grid movement contract. Dijkstra separately sets the starting distance to zero, so the starting cell's stored entry cost is not charged initially.

If the start is isolated, it remains -1; because the target is different, the target is unreachable and the method returns -1 before Dijkstra.

**Build the weighted graph implicitly**

Once exploration ends, every reachable coordinate except the isolated-start case has a nonnegative cost. Moving from one discovered cell to a neighboring discovered cell costs `g[nx][ny]`, the cost of entering the destination. The start's cost is omitted because Dijkstra begins with distance zero there.

If `target` was never changed from `(-1,-1)`, DFS never reached it, so no valid path exists and -1 is returned.

**Run Dijkstra on the discovered cells**

The priority queue begins with `(0, sx, sy)`. Array `dist` stores the best known total cost, with zero at the start and infinity elsewhere.

When `(w,x,y)` is removed, reaching `target` allows immediate return of `w`. For every four-neighbor discovered cell, candidate cost is

`w + g[nx][ny]`.

If this improves `dist[nx][ny]`, the distance is updated and pushed.

All entry costs are positive on traversable cells, so the first target entry removed from the min-heap has minimum possible total cost.

The source does not explicitly discard stale heap entries. Such entries may rescan up to four neighbors, but a smaller queued entry is removed first and performs any useful relaxations. Bounded grid degree keeps this extra work within the standard sparse-graph bound.

**Why the combined method is correct**

Reversible DFS visits every cell reachable from the start: if a reachable unvisited neighbor exists, `canMove` permits it and recursion explores it. It records exactly the cost of entering each discovered coordinate and records the target if reachable.

The resulting coordinate graph has the same reachable adjacencies and movement costs as the hidden grid. Dijkstra is correct for its nonnegative edge costs, and its path total charges every entered cell while excluding the initial cell. Therefore the returned distance is exactly the minimum interactive-grid path cost.

## Complexity detail

Let $V$ be the number of reachable cells and $E$ their adjacencies. Grid degree is at most four, so $E=O(V)$.

DFS performs constant direction work per discovered cell and traverses each exploration edge forward and backward, taking $O(V+E)=O(V)$ interactive work. Dijkstra takes $O((V+E)\log V)=O(V\log V)$ time. This matches the manifest.

The map, distance table, heap, and recursion state use $O(V)$ conceptually. The exact source allocates fixed 200 by 200 arrays, bounded by the constraints. DFS recursion depth can reach $O(V)$ and may exceed Python's usual recursion limit on a long corridor; an iterative exploration would avoid that runtime risk.

## Alternatives and edge cases

- **Dijkstra while physically exploring:** It is difficult to preserve heap order while the robot occupies only one cell; mapping first cleanly separates concerns.
- **Breadth-first search after mapping:** It minimizes moves, not total cost, and is wrong when cell costs differ.
- **Iterative DFS:** An explicit stack can preserve backtracking actions while avoiding recursion-depth failure.
- **Mark the start immediately:** Using a separate visited structure or a special start marker avoids the exact source's one redundant start rediscovery.
- **Stale-entry guard:** Skipping when `w != dist[x][y]` avoids unnecessary Dijkstra neighbor scans.
- **Target unreachable:** DFS never records it and the method returns -1.
- **Start cost:** It is not charged because the initial heap distance is zero.
- **Re-entering the start later:** Its recorded cell cost is correctly charged when a path moves back into it.
- **Blocked or off-grid neighbor:** `canMove` prevents movement and the cell remains undiscovered.
- **Target different from start:** The contract removes the zero-move target case.
- **Backtracking direction:** Adding two modulo four maps U to D and R to L.
- **Fixed coordinate padding:** Centering at 100 safely represents every relative location in a grid of dimension at most 100.
- **Positive costs:** They justify Dijkstra and early return on the first target pop.
- **Physical-state invariant:** Every recursive call must backtrack before returning, or later coordinates would no longer match the robot.
- **API ownership:** `GridMaster` is provided by the platform and is not implemented by the solution.
