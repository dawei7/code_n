## General

**Convert adjacent ones into edges that must be covered**

Create one graph vertex for every grid cell containing 1. Connect two vertices when their cells are horizontally or vertically adjacent.

To make the grid well-isolated, every such adjacency edge must lose at least one endpoint: flipping either endpoint from 1 to 0 removes that conflict.

Choosing the minimum cells to flip is therefore the minimum vertex cover problem on this adjacency graph.

**Use checkerboard parity to obtain a bipartite graph**

Every horizontal or vertical move changes the parity of `row + column`. Thus every adjacency connects an odd-parity cell to an even-parity cell.

The graph is bipartite. The source builds adjacency only from odd-parity 1-cells to neighboring even-parity 1-cells. Each conflict edge is represented once.

Cell coordinates are flattened to `x = i * n + j`, giving compact integer vertex identifiers.

**Relate minimum flips to maximum matching**

Kőnig's theorem states that in a bipartite graph, the size of a minimum vertex cover equals the size of a maximum matching.

Therefore, the method does not need to explicitly construct which cells form the cover. It only needs the maximum number of vertex-disjoint adjacency edges.

That matching size is the minimum number of flips.

**Find augmenting paths with DFS**

`match[j]` stores the odd-side vertex currently matched to even-side vertex `j`, or `-1` if none.

For one odd vertex `i`, `find(i)` tries its adjacent even vertices. `vis` prevents revisiting the same even vertex within this augmentation attempt.

If neighbor `j` is unmatched, it can be assigned immediately. If it is matched, the recursion tries to reroute its current odd partner to another neighbor. When rerouting succeeds, `j` becomes available for `i`.

Returning 1 means the matching grew by one. The outer loop resets `vis` for every odd start and adds the result to `ans`.

**Why rerouting is necessary**

A greedy match to the first free neighbor can block a later vertex even when a larger matching exists. An augmenting path alternates between unused and used edges, shifting earlier assignments and increasing total matching size by one.

The recursive `find(match[j])` performs exactly this alternating reroute.

**Why the returned matching size is the answer**

Repeatedly finding augmenting paths until every odd-side vertex has been attempted produces a maximum bipartite matching under the standard Kuhn algorithm argument: if no augmenting path remains, no larger matching exists.

Kőnig's theorem converts that maximum matching cardinality to the minimum vertex-cover cardinality. Flipping those cover vertices removes every adjacency, while fewer flips could not cover all matched edges because matched edges have disjoint endpoints.

Thus `ans` is exactly the minimum operation count.

Isolated 1-cells produce no edges, are absent from `g`, and require no flip.

**Be precise about the exact matching algorithm**

The manifest describes Hopcroft–Karp and claims $O(E\sqrt V)$ time. The exact source does not perform BFS layering or batch shortest augmenting paths.

It runs a fresh DFS augmentation from each left vertex, which is the Kuhn algorithm. Its conservative worst-case time is $O(VE)$, though grid degree is at most four and practical behavior may be good.

The documentation must analyze these executable loops rather than name an algorithm that is not implemented.

## Complexity detail

Let $V$ be the number of 1-cells and $E$ the number of horizontal/vertical adjacencies between them.

Graph construction is $O(V+E)$. Up to $O(V)$ left vertices each run a DFS that can inspect $O(E)$ edges through rerouting, giving $O(VE)$ worst-case time for the exact source.

The adjacency lists use $O(V+E)$ space, `match` uses $O(mn)$ entries, and one visited set plus recursion stack uses $O(V)$. Since grid cells bound vertices, total space is $O(mn+E)$, commonly written $O(V+E)$ if only active graph vertices are allocated; the exact dense `match` array makes the $mn$ term explicit.

## Alternatives and edge cases

- **Hopcroft–Karp:** BFS layers plus DFS augmentations achieve $O(E\sqrt V)$ and would match the manifest, but those layers are absent from the source.
- **Flip every cell with a neighbor:** This covers all edges but can use far more flips than a minimum vertex cover.
- **Greedy local flipping:** Choices interact across adjacent edges and need not be optimal.
- **All-zero grid:** The graph is empty and the result is zero.
- **Diagonal ones:** They are not 4-directionally adjacent, so no edge connects them.
- **Single isolated one:** No operation is needed.
- **Long chain of ones:** Matching captures alternating cells as the minimum cover size.
- **Checkerboard parity:** Every valid adjacency crosses sides; no same-side edge exists.
- **Visited reset:** It must be fresh per augmenting attempt, or valid rerouting paths may be blocked.
- **Flattened identifiers:** `i * n + j` uniquely represents every cell.
- **Recursion depth:** A long augmenting path can be a practical Python recursion concern.
- **Manifest mismatch:** Exact worst-case time is $O(VE)$ for DFS augmentation, not Hopcroft–Karp's $O(E\sqrt V)$.
