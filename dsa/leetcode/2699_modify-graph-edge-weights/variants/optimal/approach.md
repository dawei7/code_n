## General

Store each undirected adjacency as `(neighbor, edge_index)` so both directions refer to the same mutable row in `edges`. The problem then becomes choosing each unknown weight while preserving enough shortest-path information to avoid repeatedly solving the graph from scratch.

**Optimistic distances to the destination**

First run Dijkstra's algorithm from `destination`, temporarily treating every `-1` edge as weight $1$, its smallest legal value. Let `lower[v]` be the resulting distance from vertex $v$ to the destination. These are lower bounds for every eventual assignment because unknown weights can only stay at $1$ or increase.

If `lower[source] > target`, even the smallest legal assignment is too long, so no answer exists.

**Assign slack during a second Dijkstra pass**

Run Dijkstra again from `source`. When a settled vertex `u` reaches a still-unknown edge to `v`, let `dist[u]` be the finalized prefix distance. Assign

$$
w = \max\bigl(1,\ \texttt{target} - \texttt{dist}[u] - \texttt{lower}[v]\bigr).
$$

If the prefix plus the optimistic suffix is already at least the target, weight $1$ is sufficient. Otherwise this formula puts exactly the missing slack on the current edge. The assignment ensures that the route represented by this settled prefix, the edge, and any optimistic suffix from `v` cannot be shorter than the target.

A lower-bound shortest path that contains an unknown edge can absorb the required slack at the first such edge encountered from a settled prefix; its remaining lower-bound edges may stay at their minimums, retaining a route of length exactly `target`. If a route made only of fixed edges remains shorter, no assignment can remove it. The second Dijkstra pass exposes that obstruction because its final destination distance will be below `target`.

After the pass, return the edges only when the computed destination distance is exactly `target`. Assign any still-unseen unknown edge the legal maximum $2 \cdot 10^9$ so it cannot introduce a new short route. Fixed positive edges are never changed.

## Complexity detail

Let $m = \lvert\texttt{edges}\rvert$. Building the adjacency structure takes $O(n+m)$ time and space. Each of the two Dijkstra passes processes $n$ vertices and $m$ undirected edges with a binary heap, taking $O((n+m)\log n)$ time. The graph, distance arrays, and heap use $O(n+m)$ space.

## Alternatives and edge cases

- **Enable unknown edges one by one:** Rerunning Dijkstra after every newly assigned edge is correct, but with $k$ unknown edges it costs $O(k(n+m)\log n)$.
- **Bellman-Ford relaxation:** It can recompute shortest paths with nonnegative assigned weights, but $O(nm)$ per run is unnecessary.
- **Independent binary searches:** Unknown weights interact across competing paths, so optimizing each edge separately does not provide a monotone one-dimensional search.
- If the all-ones lower bound already exceeds `target`, increasing weights cannot help.
- A fixed-only path shorter than `target` makes the request impossible because its edges cannot be increased.
- The target may already be achieved without changing any shortest path; remaining unknown edges can then receive sufficiently large values.
- Many valid assignments and edge orders may exist, so correctness must validate the graph semantics rather than compare against one exact output list.
