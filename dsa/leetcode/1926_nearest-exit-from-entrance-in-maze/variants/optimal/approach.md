## General
**Explore in increasing distance**

Run breadth-first search from the entrance. The queue initially contains the entrance at distance zero. When a cell is removed, inspect its four neighbors. Ignore coordinates outside the grid, walls, and cells already visited.

Mark a cell visited as soon as it is enqueued rather than when it is removed. This prevents two frontier cells from adding the same location and ensures each open cell is processed at most once.

**Recognize exits without accepting the entrance**

Mark the entrance before the search begins. For each newly discovered open neighbor, test whether its row is `0` or `R - 1`, or its column is `0` or `C - 1`. If so, return the current distance plus one.

Because BFS processes all cells at distance $d$ before any cell at distance $d+1$, the first discovered exit has the minimum possible path length. The entrance is never reconsidered, so a boundary entrance cannot be mistaken for a zero-step exit. If the queue empties, every reachable open cell has been examined and no exit exists.

## Complexity detail
At most $RC$ cells enter the queue, and each checks four constant-time directions, giving $O(RC)$ time. The queue and visited state can each hold $O(RC)$ cells, so the space bound is $O(RC)$. The implementation reuses the maze to mark visited cells but the queue alone can still require linear space.

## Alternatives and edge cases
- **Depth-first search for the first exit:** The first exit found by DFS need not be the nearest.
- **Repeated distance relaxation:** Bellman-Ford-style full-grid passes eventually find shortest distances but can require many scans.
- **Mark on dequeue:** This permits duplicate queue entries and wastes work.
- **Boundary entrance:** It is explicitly excluded, so at least one move is required.
- **Single-cell maze:** The only cell is the entrance, leaving no exit.
- **Several exits:** BFS returns the minimum distance without needing to enumerate all complete paths.
- **Sealed open region:** Exhausting the queue correctly returns `-1`.
