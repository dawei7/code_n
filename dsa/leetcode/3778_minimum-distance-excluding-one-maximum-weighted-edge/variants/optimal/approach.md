## General

For a fixed path, omitting one edge minimizes the remaining sum precisely when the omitted edge has maximum weight. If several path edges share that maximum, omitting the first one or any other tied one produces the same numerical cost. Therefore the problem is equivalent to finding a path whose traversal may make exactly one edge free.

Represent each graph node with two states: `(node, 0)` before an edge has been excluded and `(node, 1)` afterward. From either state, traversing an edge normally adds its weight. From an unused state, one additional transition crosses that same edge at zero cost and enters the used state.

Run Dijkstra's algorithm on this two-layer state graph. All transition costs are non-negative, so when `(n - 1, 1)` is removed from the priority queue with its current best distance, that cost is final. Requiring the second layer at the destination also enforces that exactly one path edge was excluded.

Every route in the expanded graph projects to a source-to-target walk with one free edge. Removing positive-cost cycles cannot worsen it, so some simple path has no greater cost. Conversely, any legal path is represented by taking paid transitions for all of its edges except the chosen maximum edge, where it takes the free transition. The state search therefore considers an optimal realization of every legal path and returns the requested minimum.

## Complexity detail

Let $N$ be the number of nodes and $E$ the number of edges. Two adjacency-list Dijkstra runs and one edge scan take $O((N+E)\log N)$ time. The graph, two distance arrays, and priority queue use $O(N+E)$ space.

## Alternatives and edge cases

- **Two ordinary Dijkstra runs:** Compute distances from both endpoints, then scan every edge as the free edge in both orientations. This has the same asymptotic bounds, but the two-layer state graph expresses the one-time exclusion directly.
- **Repeated minimum selection:** Replacing each priority queue with a linear search over unsettled nodes remains correct but raises Dijkstra's cost to $O(N^2+E)$.
- **Single-edge path:** Its only edge is necessarily excluded, so a direct edge from `0` to `n - 1` makes the answer `0`.
- **Tied maximum edges:** Only one is omitted. Choosing the first tied occurrence satisfies the rule, while all later equal-weight edges remain paid.
- **Longer ordinary path:** A path with a larger unmodified weight sum may still win after its largest edge is excluded.
- **Undirected input:** Each edge must be added in both traversal directions even though its stored endpoints obey $u_i<v_i$.
- **Large result:** The sum of paid weights may require a wider integer type than an individual edge weight.
