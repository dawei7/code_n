## General

**Turning edge classification into controlled MST experiments**

All minimum spanning trees have the same total weight, even when their edge sets differ. This lets the stored solution classify an edge by comparing constrained Kruskal runs with the ordinary minimum weight.

An edge is critical if removing it makes the graph disconnected or makes the cheapest remaining spanning tree heavier. It is pseudo-critical if it is not critical and there exists a minimum spanning tree that includes it. The source tests these definitions directly: exclude an edge to test necessity, then force it to test eligibility.

Before sorting, the loop appends each original position `i` to its edge record. An edge changes from three fields to four fields: endpoints, weight, and original index. The list is then sorted by weight for Kruskal's algorithm. Preserving the index is necessary because the returned identifiers refer to the original input order rather than sorted positions.

This preprocessing mutates `edges` in place by extending every inner list and reordering the outer list. That behavior does not affect the returned classification, but callers should not expect the input structure to remain unchanged.

**How the union-find supports Kruskal**

`UnionFind` starts with every vertex in its own component. The array `p` stores parent links, and `n` stores the current number of components.

`find(x)` follows parent links to a representative. On the return path, it rewrites visited links to point directly toward that representative. This path compression accelerates later searches.

`union(a, b)` first checks whether both endpoints already share a representative. If so, adding the edge would create a cycle, so it returns false. Otherwise, it attaches one representative beneath the other, decreases the component count, and returns true. The implementation does not use union by rank or size.

Kruskal scans edges from smallest to largest weight. It accepts an edge exactly when `union` joins two previously separate components. Consequently, accepted edges never form a cycle. For a connected graph, they eventually join all vertices with the minimum possible total weight.

**Computing the baseline**

The first union-find run evaluates

`sum(w for f, t, w, _ in edges if uf.union(f, t))`.

The generator calls `union` as its filter. A weight enters the sum only when that edge connects two components. The resulting value `v` is the weight of an ordinary MST. The input graph is guaranteed connected, so this run reaches one component.

**Testing whether an edge is critical**

For each sorted edge with original index `i`, the code creates a fresh union-find and reruns Kruskal while skipping the edge whose stored index equals `i`. The resulting weight is `k`.

If `uf.n > 1`, the remaining edges could not connect all vertices, so every spanning tree requires the excluded edge. It is critical.

If the graph remains connected but `k > v`, the lightest tree without the edge is more expensive than an unrestricted MST. The edge must therefore occur in every MST, so it is also critical. The code appends its original index to `ans[0]` and uses `continue` because a critical edge should not also be reported as pseudo-critical.

The condition explicitly includes `uf.n == 1` before comparing the connected result. Since `v` is the global minimum, a connected exclusion run cannot legitimately produce less than `v`.

**Testing whether an edge is pseudo-critical**

For a noncritical edge, the source creates another fresh union-find. It first executes `uf.union(f, t)` and initializes `k = w`, thereby forcing the candidate edge into the tree before considering any others. It then runs Kruskal over all other edges.

If the forced run finishes with total weight `k == v`, it has explicitly constructed a spanning tree that contains the candidate and has minimum weight. That is exactly the evidence required for pseudo-critical status, so the original index is appended to `ans[1]`.

The graph has distinct endpoint pairs with `f < t`, so the initially forced edge is not a self-loop and its union succeeds. Because the candidate was already joined, skipping it in the remaining scan also prevents its weight from being counted twice.

**Why the two tests are complete**

If exclusion disconnects the graph or raises its best tree weight, no MST can omit the edge; it is critical by definition. Conversely, if exclusion still permits weight `v`, at least one MST omits it, so it is not critical.

For such a noncritical edge, forcing it and obtaining weight `v` proves that at least one MST contains it. If the cheapest forced tree is heavier, no MST can contain it. Thus every edge is placed in precisely the appropriate output group or left out when it belongs to no MST.

## Complexity detail

Let $V$ be the number of vertices and $E$ the number of edges. Appending indices costs $O(E)$, and sorting costs $O(E \log E)$. The baseline Kruskal run scans $E$ edges.

The classification loop is the dominant work. For each of $E$ candidate edges, it performs one full exclusion scan. For every noncritical edge, it performs a second full forced scan. Therefore, it executes $O(E^2)$ union-find operations overall.

The editorial's familiar bound with union by rank and path compression is $O(E^2 \alpha(V))$, where $\alpha$ is the inverse Ackermann function. The exact stored `UnionFind` uses path compression but does not use rank or size when linking roots, so that precise combined-heuristic bound should not be claimed without qualification. A conservative description is $O(E^2 \log V + E \log E)$ amortized for these disjoint-set operations, while in practice path compression makes them very fast on the stated limits.

Most importantly, the exact source does not meet the manifest's $O(E \log E)$ time. That faster bound requires a different classification algorithm that processes equal-weight edge groups and finds bridges in contracted component graphs. Repeated Kruskal is quadratic in $E$ regardless of how fast each individual union-find operation becomes.

The mutated edge records occupy $O(E)$ input storage, each fresh union-find uses $O(V)$ arrays, and the returned lists use $O(E)$. Only one temporary union-find exists at a time, so auxiliary space is $O(V)$ beyond the modified input and output, or $O(V + E)$ when those structures are included.

## Alternatives and edge cases

- **Weight-group bridge classification:** Process edges of equal weight together after contracting components formed by lighter edges, then find bridges in the temporary multigraph. This can achieve the manifest's $O(E \log E)$ target but is substantially more intricate.
- **Repeated Kruskal with rank and path compression:** This matches the editorial's near-constant union operations but remains $O(E^2 \alpha(V))$, not $O(E \log E)$.
- **Enumerating all spanning trees:** It can classify edges by direct observation but is exponential and unnecessary.
- **Unique MST:** Every edge in that one MST is critical, while edges outside it are neither critical nor pseudo-critical.
- **All equal-weight cycle:** No one cycle edge is required, but each can appear in some MST, so those edges are pseudo-critical.
- **Edge in no MST:** Its forced run has weight greater than `v`, so it belongs to neither output list.
- **Exclusion disconnects the graph:** Component count remains above one, and the edge is critical even if the partial forest's numeric weight is small.
- **Original indices:** Sorting changes positions, so appending indices before sorting is essential for returning the requested identifiers.
- **Input mutation:** The source appends a fourth field and sorts the provided list. Reusing the original three-field order afterward would be unsafe.
- **Equal weights:** Python's stable ordering is not needed for correctness; Kruskal may choose any safe edge among equal weights.
- **No union by rank:** Path compression is present, but the data structure can temporarily build less balanced parent trees than a fully optimized implementation.
