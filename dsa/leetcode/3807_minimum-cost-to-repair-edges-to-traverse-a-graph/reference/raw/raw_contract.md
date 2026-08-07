## Function Contract

**Inputs**

- `n`: The number of graph nodes, labeled `0` through `n - 1`.
- `edges`: An array of triples `[u, v, w]` describing undirected edges and their positive repair costs.
- `k`: The maximum number of edges allowed in the route from the source to the destination.

Let $N=n$ and $M=\lvert\texttt{edges}\rvert$. Selecting `money` repairs all edges with $w\leq\texttt{money}` simultaneously; individual edges cannot be purchased separately. A valid route may contain fewer than `k` edges.

**Return value**

Return the minimum repair threshold that permits a route from node `0` to node `n - 1` within the edge limit. Return `-1` if the destination is unreachable within `k` edges even after every edge is repaired.
