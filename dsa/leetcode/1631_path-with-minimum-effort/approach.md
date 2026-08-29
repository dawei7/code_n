## General

**Turn the grid into a weighted undirected graph**

Each cell is a graph vertex. Two horizontally or vertically adjacent cells share an edge whose weight is the absolute difference between their heights. A grid route is then a graph path, and the route's effort is the maximum edge weight used on that path.

This is a bottleneck-path objective. Adding all edge weights is wrong: a path with many small changes can be better than a short path containing one large jump. The source seeks the smallest threshold $H$ for which the start and destination become connected using only edges of weight at most $H$.

The grid has `m` rows and `n` columns. Cell `(i, j)` is flattened to integer

$$
i\cdot n+j.
$$

This maps the top-left cell to 0 and the bottom-right cell to $mn-1$, giving the disjoint-set structure simple contiguous identifiers.

**Create every undirected adjacency exactly once**

`dirs = (0, 1, 0)` may look unusual. Applying `pairwise(dirs)` yields exactly two direction pairs:

`(0, 1)` and `(1, 0)`.

These are the right and down directions. From each cell, the loops therefore consider only its right neighbor and its lower neighbor when those coordinates are in bounds.

That is sufficient because grid edges are undirected. The left edge of one cell is already the right edge generated from its left neighbor, and the upper edge is already the down edge generated from its upper neighbor. Including all four directions would duplicate every edge without adding connectivity information.

For each valid neighbor, the source appends a tuple containing the absolute height difference and the two flattened endpoints. If the grid has $V=mn$ cells, the exact edge count is

$$
E=m(n-1)+(m-1)n,
$$

which is $O(V)$.

**Process edges from the easiest to the hardest**

`e.sort()` orders tuples primarily by their first component, the height difference. Endpoint IDs only break ties and do not affect correctness.

The source then performs a Kruskal-style sweep. Initially every cell is in its own disjoint-set component. For each sorted edge `(h, a, b)`, it unions the endpoint components. Immediately afterward, it asks whether vertex 0 and vertex $mn-1$ are connected.

At that moment, every processed edge has weight at most `h`. If start and destination have just become connected, there is a path composed entirely of processed edges, so every step on that path has difference at most `h`. The path effort is therefore at most `h`.

Because edges were processed in non-decreasing order, no smaller threshold could have connected the endpoints earlier. Thus the first `h` that produces connectivity is exactly the minimum possible effort, and the method returns it immediately.

**How Union-Find maintains components**

`UnionFind` stores a parent array `p` and component sizes. Initially every vertex is its own root.

`find(x)` recursively follows parents. On its way back, path compression rewrites each visited parent directly to the root. `union(a, b)` obtains both roots and does nothing if they already match. Otherwise, it attaches the smaller component below the larger component and updates the winning root's size. When sizes tie, the source chooses the second root.

These two heuristics make the component operations amortized almost constant time. More importantly, the DSU represents exactly the connected components formed by the prefix of sorted edges processed so far.

**The threshold equivalence behind correctness**

For any non-negative number $H$, form a subgraph containing exactly grid edges whose weight is at most $H$. There exists a route of effort at most $H$ if and only if the start and destination are connected in this subgraph:

- If such a route exists, every edge on it has weight at most $H$, so the route is present in the subgraph.
- If the vertices are connected in the subgraph, the connecting path uses only edges of weight at most $H$, so its maximum edge weight is at most $H$.

The sorted sweep considers thresholds only at actual edge weights, which are the only points where connectivity can change. Just after processing an edge of weight `h`, DSU represents the relevant threshold subgraph, possibly partway through other edges tied at `h`. If connectivity already holds, those processed edges provide a valid effort-`h` path. If a lower threshold could work, connectivity would have occurred before any weight-`h` edge was reached. The first returned weight is therefore optimal.

This is closely related to a minimum spanning tree property: the unique tree path between two vertices in a minimum spanning tree minimizes the largest edge needed. The source does not need to finish building a whole spanning tree; it stops as soon as its two target vertices share a component.

**Single-cell behavior**

When the grid has one cell, the start already equals the destination and no move is needed. No edges are generated, so the loop never returns and the final `return 0` supplies the correct zero effort.

For any larger rectangular grid, right/down adjacencies make the full grid graph connected. After all edges are processed, the endpoints must share a component, so the return inside the loop is reached. The trailing zero remains a valid safety return as well as the necessary one-cell result.

## Complexity detail

Let $V=mn$ and $E=m(n-1)+(m-1)n$. Building the edge list costs $O(E)$ time and space. Since $E=O(V)$ for a grid, sorting costs

$$
O(E\log E)=O(V\log V).
$$

Each processed edge performs a constant number of Union-Find operations. With union by size and path compression, each costs amortized $O(\alpha(V))$, so the sweep costs $O(E\alpha(V))$. Sorting dominates, giving total time $O(V\log V)$.

The edge list holds $O(V)$ tuples. The parent and size arrays each hold $V$ integers. Path-compressed recursion has at most small tree depth under union by size, bounded by $O(\log V)$ even before compression. Total auxiliary space is $O(V)$, matching the manifest.

The source may stop before processing every edge, which improves practical time but not the worst-case bound. Tuple sorting uses endpoint values only as deterministic tie breakers after effort.

## Alternatives and edge cases

- **Modified Dijkstra algorithm:** Store for each cell the smallest known maximum edge on a path from the start, and relax a neighbor with `max(current_effort, edge_weight)`. This also runs in $O(V\log V)$ on a grid and can stop when the destination leaves the heap.
- **Binary search plus graph traversal:** Test whether the destination is reachable using only edges at most a candidate threshold. Monotonicity permits binary search over height differences, costing $O(V\log H)$ where $H$ is the difference range.
- **Minimum spanning tree construction:** Finish Kruskal, then inspect the tree path. The source uses the same property more efficiently by stopping at the first moment the two relevant vertices connect.
- **Ordinary shortest-path sums:** Summing height differences optimizes a different objective. The required route cost is the maximum single difference.
- **Generate four directions:** It remains correct with a visited-edge strategy, but naïvely adds every undirected edge twice and increases constants.
- **One row or one column:** The edge generator creates the single chain of horizontal or vertical adjacencies. The maximum edge on that only route is returned.
- **One cell:** There are no edges and the correct effort is zero, handled by the final return.
- **Equal neighboring heights:** Their edge weight is zero. A complete zero-weight route makes the endpoints connect while processing weight-zero edges and returns zero.
- **Several edges have the same weight:** Their internal order is irrelevant. If connectivity occurs after any one of them, the current threshold is still that shared weight.
- **Flattening formula:** The multiplier must be the column count `n`, not the row count. This gives every grid coordinate a unique ID from 0 through $mn-1$.
- **Bounds checks:** Right and down neighbors outside the grid are skipped, preventing nonexistent wraparound edges.
- **Already connected edge endpoints:** `union` returns false and changes nothing. Redundant cycle edges do not harm the connectivity test.
