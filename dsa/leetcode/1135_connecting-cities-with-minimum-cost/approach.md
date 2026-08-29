## General

**The problem asks for a minimum spanning tree**

Cities are graph vertices and available bidirectional connections are weighted edges. Connecting every city with minimum total selected cost is exactly the minimum spanning tree problem when the graph is connected.

Kruskal’s algorithm considers edges from cheapest to most expensive and accepts an edge only when it connects two currently separate components.

**Sort by connection cost**

`connections.sort(key=lambda x: x[2])` orders edges by their third field. It sorts the caller’s list in place.

Parallel edges remain independent. The cheaper one is considered first; a later parallel edge will be skipped if its endpoints are already connected.

**Track components with disjoint-set union**

Parent array `p` uses zero-based city indices. Input labels are converted with `x - 1` and `y - 1`.

`find` follows parents to a representative root and applies path compression, making later searches shorter.

If two endpoints already have equal roots, adding their edge would create a cycle. A cycle is unnecessary for connectivity and adds nonnegative cost, so the edge is skipped.

If roots differ, `p[find(x)] = find(y)` merges the components and `cost` is added to `ans`.

The parent assignment uses representatives rather than raw endpoint indices. Attaching a non-root endpoint directly could fail to merge the complete components or leave an inconsistent forest.

**Use the local `n` as a component count**

Initially there are `n` singleton components. Every successful union reduces that count by one. Redundant edges do not.

When the count reaches one, every city is connected. The algorithm returns immediately because later edges are no cheaper and cannot improve an already complete spanning tree.

If all edges are exhausted with more than one component, no available edge can bridge the remaining groups, so the method returns `-1`.

Every successful union reduces the component count exactly once because root inequality is checked first. This count is equivalent to tracking how many spanning-tree edges have been accepted: after `n-1` successful unions, one component remains.

**Why choosing the cheapest bridge is safe**

When Kruskal selects an edge connecting two components, consider any optimal spanning tree that does not contain it. Adding the selected edge creates a cycle. That cycle contains another edge crossing the same component cut.

Because the selected edge is the cheapest remaining crossing candidate, replacing the other edge cannot increase total cost. Therefore, some optimal tree includes every greedy choice. Repeating the exchange proves the completed tree is minimum-cost.

Skipping an edge whose endpoints already share a root is also safe. The accepted edges already contain a path between those endpoints, so adding the edge creates a cycle. Removing the skipped edge from that cycle leaves connectivity unchanged and never raises the selected cost because the edge was never needed.

**Implementation nuances**

The code uses path compression but no union-by-rank or size. It is efficient under constraints, though the classical inverse-Ackermann DSU guarantee normally combines both techniques.

The exact code also does not return zero before scanning when `n == 1`. It returns only after a successful union lowers the component count. Under a natural graph contract, one city is already connected and should cost zero.

The local constraints simultaneously require `n >= 1`, at least one connection, and distinct endpoints within one through `n`, leaving no valid connection input when `n = 1`. If that boundary were represented with an empty connection list, the protected code would return `-1` instead of zero. A robust implementation should handle it explicitly.

Variable `n` changes meaning after initialization: it begins as the city count and is then used as the live component count. City-label conversion and parent allocation occur before any decrement, so this reuse does not affect indexing.

## Complexity detail

Let $m$ be connection count. Parent initialization costs $O(n)$ and sorting costs $O(m\log m)$.

With path compression and rank, DSU work is $O(m\alpha(n))$. This exact source omits rank, so a conservative formal bound includes a weaker DSU term such as $O(m\log n)$ amortized, though sorting commonly dominates.

The sorted list occupies $O(m)$ input storage and Python sorting may use temporary memory. Parent storage is $O(n)$, yielding the manifest’s $O(n+m)$ space description.

## Alternatives and edge cases

- **Prim’s algorithm:** Grow one tree with a priority queue in $O(m\log n)$ time; convenient with adjacency lists.
- **Union by rank:** Add component sizes or ranks to strengthen the DSU bound and tree shape.
- **Cycle acceptance:** Incorrect because it adds cost without connecting new components.
- **Disconnected graph:** Component count remains above one and the result is `-1`.
- **Parallel connections:** Kruskal naturally prefers the cheapest useful one.
- **Zero-cost edge:** It is considered first and safely accepted if it joins components.
- **Already connected endpoints:** The edge is skipped regardless of cost.
- **Exactly `n-1` successful unions:** Any connected spanning tree on `n` cities has this many edges.
- **One city:** Mathematically costs zero; the exact code needs an early return to support that boundary.
- **Input mutation:** Sorting permanently reorders `connections`.
- **One-based labels:** Subtracting one aligns them with the parent array.
- **Equal-cost edges:** Any order among them can lead to a minimum spanning tree.
