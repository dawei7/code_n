## General
**Compress each subdivided chain into one weighted edge**

Traveling from one original endpoint to the other crosses `cnt + 1` unit edges. Build an adjacency list on only the $n$ original nodes with that weight, then run Dijkstra's algorithm from node `0`. Every original node whose finalized distance is at most `maxMoves` contributes one to the answer.

**Count each chain from both reachable ends**

For an original node `u` at distance `dist[u]`, the remaining moves available to enter an incident chain are `max(0, maxMoves - dist[u])`. For edge `[u, v, cnt]`, approaches from its two ends can cover that many new nodes from each side. The number of distinct reachable subdivision nodes on the edge is therefore `min(cnt, from_u + from_v)`.

Dijkstra gives the true shortest distance to every original endpoint because all compressed weights are positive. Any path to a subdivision node must enter its chain through one endpoint, so the remaining-move counts describe exactly the reachable prefix from each side. Adding those prefixes and capping at `cnt` counts their union once even when they overlap.

## Complexity detail
Building and scanning the adjacency list costs $O(n+m)$. Dijkstra performs $O(n+m)$ heap operations at $O(\log n)$ each, for $O((n+m)\log n)$ time. Distances, the heap, and adjacency entries use $O(n+m)$ space.

## Alternatives and edge cases
- **Expand every subdivision node:** Ordinary BFS is correct on the expanded graph but can require time and space proportional to $\sum \texttt{cnt}$, which may be enormous.
- **Unweighted BFS on original nodes:** Original edges represent different chain lengths, so treating them equally gives incorrect distances.
- **Bellman-Ford:** It handles the positive weights but costs $O(nm)$ time.
- **Zero subdivisions:** The edge contributes no new nodes but still connects its endpoints with weight one.
- **Partial chain reach:** Reaching some new nodes does not imply reaching the opposite original endpoint.
- **Approach from both ends:** Cap their combined coverage at `cnt` to avoid double-counting overlap.
- **Disconnected node zero:** Node `0` itself is always reachable even when no edge is incident to it.
