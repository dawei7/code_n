## General

For a fixed path, omitting one edge minimizes the remaining sum precisely when the omitted edge has maximum weight. If several path edges share that maximum, omitting the first one or any other tied one produces the same numerical cost. Therefore the problem is equivalent to finding a path whose traversal may make exactly one edge free.

Run ordinary Dijkstra searches from node `0` and from node `n - 1`. Let the resulting distances be `from_start` and `from_target`. If an edge `(u, v)` is made free and traversed from `u` to `v`, the best corresponding cost is `from_start[u] + from_target[v]`; the reverse orientation costs `from_start[v] + from_target[u]`. Evaluate both orientations of every edge and take the minimum.

Each evaluated expression constructs a source-to-target walk with one free edge. Since every paid edge has positive weight, deleting any cycle cannot increase its cost; if simplification removes the designated free edge, some remaining path edge can instead be omitted and only improve the result. Conversely, every legal path appears among the candidates when its omitted maximum edge is evaluated in its traversal direction. The minimum candidate is consequently exactly the requested minimum path cost.

## Complexity detail

Let $N$ be the number of nodes and $E$ the number of edges. Two adjacency-list Dijkstra runs and one edge scan take $O((N+E)\log N)$ time. The graph, two distance arrays, and priority queue use $O(N+E)$ space.

## Alternatives and edge cases

- **Two-layer Dijkstra:** Track `(node, exclusion_used)` states, with ordinary paid transitions and one zero-cost transition before the exclusion is used. This has the same asymptotic bounds and is the exact native Accepted formulation.
- **Repeated minimum selection:** Replacing each priority queue with a linear search over unsettled nodes remains correct but raises Dijkstra's cost to $O(N^2+E)$.
- **Single-edge path:** Its only edge is necessarily excluded, so a direct edge from `0` to `n - 1` makes the answer `0`.
- **Tied maximum edges:** Only one is omitted. Choosing the first tied occurrence satisfies the rule, while all later equal-weight edges remain paid.
- **Longer ordinary path:** A path with a larger unmodified weight sum may still win after its largest edge is excluded.
- **Undirected input:** Each edge must be added in both traversal directions even though its stored endpoints obey $u_i<v_i$.
- **Large result:** The sum of paid weights may require a wider integer type than an individual edge weight.
