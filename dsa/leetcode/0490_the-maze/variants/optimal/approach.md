## General

This maze is not an ordinary “move one cell at a time” reachability problem. After choosing a direction, the ball passes through every open cell in that direction and stops only immediately before a wall or boundary. It cannot turn at an intermediate cell, even if that cell is the destination. Therefore the graph nodes that matter are stopping positions, and a graph edge represents one complete roll.

The solution discovers that graph implicitly with depth-first search. `dfs(i, j)` means that the ball can stop at cell `(i, j)` and that the algorithm is now exploring every complete roll available from that stop.

**Visited means reachable as a stopping point.** At the beginning of `dfs`, `vis[i][j]` is checked. If it is already true, this stopping position has already had all four outgoing rolls explored, so repeating the work cannot discover anything new. Otherwise the cell is marked visited.

This meaning is stronger and more precise than “the ball passed through this cell.” The rolling loop may cross many open cells without marking any of them. That is correct because crossing a cell does not allow a new direction choice. In particular, passing through `destination` does not solve the problem; only a DFS call whose coordinates equal `destination` proves that the ball stopped there.

The code checks `if [i, j] == destination` after marking the cell. It then returns from that branch because no further exploration is needed to establish that this stop is reachable. The outer function does not propagate a Boolean through recursive calls. Instead, it eventually reads `vis[destination[0]][destination[1]]`. Marking before the destination check ensures this shared visited grid records success.

**Simulate one complete roll.** For each direction `(a, b)` in left, right, down, and up order, the code starts `x, y = i, j`. It repeatedly asks whether the next cell `(x + a, y + b)` is inside the grid and open. If so, it advances there. The test looks ahead before moving, so when the loop ends, `(x, y)` is still the last legal open cell, not a wall and not an out-of-bounds coordinate.

That final `(x, y)` is the only next graph node created by this direction. Calling `dfs(x, y)` explores it. If the ball cannot move at all because a wall is immediately adjacent, `(x, y)` remains `(i, j)`; the visited check returns immediately and prevents self-recursion from cycling.

The border guarantee is not required for memory safety because the loop explicitly checks bounds. It does guarantee the physical interpretation that leaving the maze behaves like hitting a wall.

**Why the DFS answers the reachability question.** Every legal decision sequence is a sequence of stopping positions. From each reachable stop, the algorithm simulates all four possible rolls exactly until their required stopping cells. Thus every legal outgoing edge is explored. Conversely, every recursive edge corresponds to a legal full roll, so DFS never invents a stop the ball cannot reach.

The start cell is a valid initial stopping position, so `dfs(start[0], start[1])` begins at the correct graph node. Standard graph-search reasoning now applies: DFS reaches exactly the nodes connected to the start in this directed stopping-position graph. The final visited lookup is true exactly when the destination belongs to that reachable set.

For the important “pass through but cannot stop” case, suppose a horizontal roll crosses the destination and continues until a wall several cells later. The inner loop does not invoke DFS at each crossing. It invokes DFS only once, at the wall-adjacent endpoint. Therefore the destination remains unvisited unless some other roll ends there, matching the contract exactly.

The solution uses recursion only for stop positions, not for every traversed cell. This distinction keeps the logical state space bounded by the number of open cells and prevents a long roll from being mistaken for a chain of direction choices.

**What the exact source does not precompute.** The optimal manifest summary says that row and column stopping endpoints are precomputed. The source shown here does not contain such tables. It rescans along a row or column every time an unvisited stop explores a direction. The algorithm is still a correct implicit graph traversal, but its implementation and strict worst-case analysis must be described as rolling-on-demand rather than endpoint-precomputed DFS.

## Complexity detail

Let $R$ be the row count and $C$ the column count. The visited matrix costs $O(RC)$ initialization and storage. At most $RC$ cells can become DFS states, and each state explores four directions.

In this exact implementation, a horizontal roll can scan $O(C)$ cells and a vertical roll can scan $O(R)$ cells. A conservative worst-case bound is therefore $O(RC(R+C))$ time. Many presentations quote $O(RC)$ for this DFS by treating a roll as a constant-cost edge computation or assuming amortized corridor traversal, but the source does not cache endpoints, and the same corridor cells can be scanned from multiple stopping states.

The recursion stack can contain $O(RC)$ stops in a worst-case depth-first path, and `vis` itself is $O(RC)$, so space is $O(RC)$. If the four stopping endpoints for every cell were precomputed in $O(RC)$ time with directional sweeps, subsequent DFS edges would be constant-time and the manifest's advertised $O(RC)$ time would be directly justified.

## Alternatives and edge cases

- **Precompute stopping endpoints:** Sweep rows and columns to record where a roll from every open cell ends in each direction. This uses $O(RC)$ extra data and makes the graph traversal itself $O(RC)$, matching the manifest summary.
- **Breadth-first search:** A queue explores the same stopping-position graph and gives the same Boolean reachability result. Shortest roll count is not requested, so BFS offers no correctness advantage over DFS.
- **Ordinary cell-by-cell DFS:** Marking every crossed cell as a decision node is wrong because the ball cannot turn there. Only wall-stopped endpoints are graph nodes.
- **Destination crossed but not stopped on:** The code correctly leaves it unvisited unless a roll ends there.
- **Direction blocked immediately:** The roll endpoint equals the current stop; the visited guard turns the resulting recursive call into constant work.
- **Cycles among stops:** The ball can roll between the same endpoints repeatedly. `vis` ensures every stop's outgoing directions are expanded once.
- **Start and destination distinction:** The contract says they differ, but the code would still return true if they were equal because the initial DFS marks the start.
- **Recursion depth:** A maze with many sequential stopping positions can create a deep Python call stack. An explicit stack preserves the same search if runtime recursion limits matter.
