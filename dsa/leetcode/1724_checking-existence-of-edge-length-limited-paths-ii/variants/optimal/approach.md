## General
**Preserve every minimum-bottleneck connection**

Sort edges by weight and run Kruskal's algorithm. Whenever an edge joins two previously separate components, add it to a minimum spanning forest. For any connected pair of nodes, the unique forest path minimizes the largest edge weight among all original-graph paths. Therefore a query is true exactly when the maximum forest edge on its path is below `limit`.

**Root each tree and record binary ancestors**

Traverse every tree in the forest to record each node's depth, immediate parent, and parent-edge weight. Build binary-lifting tables: at level $j$, store the $2^j$th ancestor and the maximum edge on that upward segment. Disjoint-set representatives retained from Kruskal identify pairs that have no path at any limit.

**Lift endpoints while accumulating the bottleneck**

For a query in one component, first lift the deeper endpoint to equal depth, updating the largest encountered weight. Then lift both endpoints from the highest binary level downward whenever their ancestors differ. Finally include the two edges to their lowest common ancestor. The collected maximum is the minimum possible path bottleneck, so return whether it is strictly less than `limit`.

## Complexity detail
Sorting $m$ edges takes $O(m\log m)$. Kruskal processing is $O(m\alpha(n))$; forest traversal and construction of $\lceil\log_2 n\rceil$ ancestor levels take $O(n\log n)$. Each of the $q$ queries examines $O(\log n)$ levels. The total time is $O(m\log m+n\log n+q\log n)$ and the forest plus lifting tables use $O(n\log n)$ space.

## Alternatives and edge cases
- **Kruskal reconstruction tree:** Create a merge node for every successful union; the weight at the lowest common ancestor of two original nodes is their minimum bottleneck, with the same logarithmic-query strategy.
- **Threshold BFS per query:** Traverse only edges below the requested limit. This is correct but can take $O(q(n+m))$ total time.
- **Persistent union-find:** Record component history by edge weight and answer each threshold query from the appropriate version, at the cost of a more specialized data structure.
- **Strict threshold:** An edge whose weight equals `limit` is forbidden.
- **Disconnected nodes:** Different minimum-spanning-forest components always return `false`.
- **Parallel edges:** Kruskal naturally keeps only an edge that improves connectivity; heavier duplicates cannot improve a bottleneck.
- **Cycles:** Edges closing a component cycle are unnecessary for every minimum-bottleneck path.
