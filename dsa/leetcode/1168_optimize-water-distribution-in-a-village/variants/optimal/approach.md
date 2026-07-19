## General
**Turn wells into graph edges.** Add a virtual water-source vertex `0`. For every house $i$, add an edge `(0, i)` weighted by `wells[i - 1]`; selecting it means building that well. Keep every offered pipe as its bidirectional edge between houses. Now every house receives water exactly when all vertices belong to the virtual source's connected component.

**Recognize a minimum spanning tree.** Any feasible selection is a connected subgraph on vertices `0..n`. If it contains a cycle, removing the most expensive edge on that cycle preserves connectivity and cannot increase cost. Therefore, an optimal selection can be a spanning tree, and its minimum cost is precisely the augmented graph's minimum spanning tree cost.

**Apply Kruskal's cut rule.** Sort all $e$ edges by cost and scan them from cheapest to most expensive. A disjoint-set structure tracks connected components. Accept an edge only when its endpoints currently have different roots, then union those roots and add its cost. The accepted edge is the cheapest edge crossing the cut between those components, so the cut property guarantees it belongs to some minimum spanning tree. Stop after accepting $n$ edges, which connects all $n+1$ vertices.

## Complexity detail
Creating the virtual well edges takes $O(n)$ time. Sorting all $e=n+p$ edges costs $O(e \log e)$; path compression and union by size add near-linear disjoint-set work within that bound. The edge list and disjoint-set arrays use $O(e)$ space in total.

## Alternatives and edge cases
- **Prim's algorithm:** Growing the augmented graph from node `0` with an adjacency list and heap also finds the MST in $O(e \log e)$ time.
- **Adjacency-matrix Prim:** Scanning all vertices for every addition is correct but takes $O(n^2)$ time, which is wasteful for sparse pipe sets.
- **Build the cheapest well only:** Pipes may form disconnected groups or be more expensive than additional wells, so one well need not suffice optimally.
- **Build every well:** This is always feasible but can ignore much cheaper pipes.
- **Parallel pipes:** Kruskal naturally considers the cheaper offer first and rejects later redundant edges if their endpoints are already connected.
- **Zero-cost choices:** Zero-cost wells and pipes are valid and should be processed before positive-cost edges.
