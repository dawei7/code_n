## General

**Turn required flips into a vertex cover**

Create one graph vertex for every cell containing `1` and one edge for every
horizontal or vertical pair of ones. A set of flips makes the matrix
well-isolated exactly when it contains at least one endpoint of every edge.
The requested minimum is therefore the graph's minimum vertex-cover size.

Color grid cells by the parity of `row + column`. Every orthogonal move changes
that parity, so every adjacency edge joins an even cell to an odd cell. The
graph is bipartite.

**Use matching to obtain the cover size**

Kőnig's theorem states that a bipartite graph's minimum vertex-cover size
equals its maximum matching size. It is consequently enough to count the
largest collection of adjacency edges that share no endpoints.

Build adjacency lists only from even-parity one-cells to neighboring odd
one-cells. Hopcroft–Karp repeatedly performs a breadth-first search from every
unmatched left vertex to layer all shortest augmenting paths, then depth-first
searches those layers to augment a maximal set of vertex-disjoint paths at
once. When no augmenting path remains, the matching is maximum.

Every matching edge needs a distinct flipped endpoint, so its size is a lower
bound on any solution. Kőnig's theorem guarantees a vertex cover of exactly
that size, and flipping that cover removes at least one endpoint of every
adjacent-one edge. The returned matching size is thus both attainable and
minimal.

## Complexity detail

Let $V=mn$ and let $E$ be the number of adjacent-one edges. Graph construction
takes $O(V+E)$ time. Hopcroft–Karp takes $O(E\sqrt V)$ time and stores the
adjacency lists, pairings, layers, and queue in $O(V+E)$ space. Grid degree is
bounded by four, but the stated bound retains both graph quantities.

## Alternatives and edge cases

- **One DFS augmenting path at a time:** Standard bipartite matching is
  correct but can take $O(VE)$ time because it rebuilds reachability for every
  left vertex instead of batching shortest paths.
- **Greedily flip a high-degree one:** Local degree choices need not form a
  minimum vertex cover and can remove more cells than necessary.
- **General maximum-flow construction:** Unit capacities also yield the
  matching, but Hopcroft–Karp is more direct for this bipartite graph.
- Diagonal ones create no edge.
- An all-zero or already isolated matrix has matching size zero.
- Separate connected components require no special handling; one matching
  naturally combines them.
- A single row or column reduces to vertex cover on disjoint paths.
