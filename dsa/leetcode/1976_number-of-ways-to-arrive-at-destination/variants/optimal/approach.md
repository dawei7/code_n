## General
**Carry path counts through Dijkstra relaxations**

Build an undirected adjacency list. Maintain `distances[v]`, the best travel
time currently known from `0` to `v`, and `ways[v]`, the number of routes that
achieve exactly that time. Initialize the source with distance zero and one
route, then process vertices through a min-heap.

For an edge from the popped vertex to `neighbor`, let `candidate` be the popped
distance plus the edge time. If `candidate` is smaller than the recorded
distance, replace the distance, copy the current vertex's path count, and push
the improved heap entry. If it ties the recorded distance, add the current
path count to the neighbor's count modulo $10^9+7$.

**Why the counted routes are exactly shortest routes**

All edge weights are positive, so when a non-stale heap entry is processed,
no later route can improve its distance. Every shortest route to a neighbor
ends with some edge from a predecessor. A strict improvement means all
previously counted neighbor routes were longer and must be discarded; each
shortest route through the new predecessor corresponds to one shortest route
to that predecessor. A tie contributes additional distinct shortest routes
without invalidating earlier ones.

Inducting over finalized distances proves that `ways[v]` counts every route of
length `distances[v]` and no longer route. The destination's count therefore
answers the problem.

## Complexity detail
The graph has $V$ vertices and $E$ roads. Building adjacency lists takes
$O(V+E)$ space and time. Each successful distance improvement adds a heap
entry, and adjacency entries are examined as vertices are processed, giving
$O((V+E)\log V)$ time. The adjacency lists, distance and count arrays, and heap
use $O(V+E)$ space.

## Alternatives and edge cases
- **Array-scanning Dijkstra:** Select the nearest unsettled vertex with a
  linear scan. It preserves the same counting relaxations but costs
  $O(V^2+E)$ time.
- **Floyd-Warshall:** All-pairs shortest paths are unnecessary for one source
  and cost $O(V^3)$ time.
- **Plain BFS:** It minimizes edge count, not total travel time, and is
  incorrect when road weights differ.
- Equal-time arrivals add route counts; a strictly faster arrival replaces
  both the old distance and its count.
- Stale heap entries must be skipped so their paths are not propagated again.
- For `n = 1`, source and destination coincide, and the empty route contributes
  one shortest way.
- Travel-time sums can exceed 32-bit range even though each individual edge
  weight fits within it.
