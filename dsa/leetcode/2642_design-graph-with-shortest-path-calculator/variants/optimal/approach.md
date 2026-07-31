## General

Store every directed edge in an adjacency list. Adding an edge then appends one pair to the source node's list and leaves all previous graph state intact.

For each `shortestPath` call, run Dijkstra's algorithm from the requested source. A distance array records the least cost discovered for each node, and a min-heap exposes the unsettled node with smallest cost. Ignore stale heap entries. Because all edge costs are positive, the first time the destination is removed with its current best distance, no later route can be cheaper, so that cost is final. If the heap empties first, no directed path reaches the destination and the method returns $-1$.

## Complexity detail

Let $n$ be the number of nodes and $e$ the current number of edges. Construction takes $O(n+e)$ time and space. `addEdge` takes $O(1)$ time. One `shortestPath` call takes $O((n+e)\log n)$ time with a binary heap and $O(n+e)$ total graph-and-query space, matching the manifest's principal query bound.

## Alternatives and edge cases

- **Floyd-Warshall:** Precomputing all-pairs distances gives $O(1)$ queries, but costs $O(n^3)$ initially and requires $O(n^2)$ work after an insertion.
- **Bellman-Ford:** Repeated relaxation handles negative weights but costs $O(ne)$ per query; every legal edge here is positive, so Dijkstra is preferable.
- **Adjacency matrix Dijkstra:** With $n \le 100$, an $O(n^2)$ query is viable, but it scans absent edges in sparse graphs.
- A node reaches itself with cost zero even when it has no incident edges.
- Edge direction matters; reachability in one direction says nothing about the reverse direction.
- Positive costs ensure cycles cannot improve a settled shortest path.
