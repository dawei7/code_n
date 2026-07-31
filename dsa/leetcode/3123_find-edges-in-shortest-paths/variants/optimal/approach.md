## General

**Decompose a shortest path around one edge.** Let $d_0[x]$ be the shortest distance from node 0 to node $x$, and let $d_t[x]$ be the shortest distance from $x$ to target node $n-1$. For an undirected edge $(u,v,w)$, traversing it from $u$ to $v$ can lie on a global shortest path exactly when

$$
d_0[u] + w + d_t[v] = d_0[n-1].
$$

The reverse orientation is possible when $d_0[v]+w+d_t[u]$ equals the same target distance.

**Compute both distance maps with Dijkstra.** All weights are positive, so run Dijkstra once from node 0 and once from node $n-1$. Then inspect every original edge in input order and test both orientations. If the target distance is infinite, return `false` for every edge; this guard also prevents arithmetic involving infinity from falsely satisfying an equality.

If an edge occurs on a shortest path, the path's prefix and suffix must themselves be shortest between their endpoints, so the corresponding equality necessarily holds. Conversely, if either equality holds, concatenating the recorded shortest prefix, that edge, and the recorded shortest suffix has exactly the global shortest length. Positive weights rule out a beneficial cycle, so the concatenation supplies a shortest path containing the edge. The test therefore marks all and only the requested edges.

## Complexity detail

Let $n$ be the number of nodes and $m$ the number of edges. The adjacency list takes $O(n+m)$ space. Each of the two heap-based Dijkstra runs costs $O((n+m)\log n)$ time and $O(n+m)$ working space, while the final edge scan costs $O(m)$. The total bounds are $O((n+m)\log n)$ time and $O(n+m)$ auxiliary space.

## Alternatives and edge cases

- **Array-based Dijkstra:** Selecting the next node by scanning every unvisited node is correct, but takes $O(n^2+m)$ time and is too slow for large sparse graphs.
- **Shortest-path DAG traversal:** After one Dijkstra run, orient tight edges by increasing distance and traverse the resulting shortest-path structure. This can work, but the two-distance equality test is direct and handles all edge orientations uniformly.
- **Breadth-first search:** BFS is valid only for equal edge weights; arbitrary positive weights require Dijkstra.
- **Disconnected target:** If node `n - 1` is unreachable from node 0, every answer entry is `false`.
- **Multiple shortest paths:** An edge is marked when it belongs to any one of them; it need not be shared by all shortest paths.
- **Undirected input orientation:** Both `u -> v` and `v -> u` equations must be checked because an edge's listed endpoint order has no direction.
- **Heavy and unrelated edges:** An edge that cannot complete the exact global shortest distance remains false even when both endpoints are reachable.
