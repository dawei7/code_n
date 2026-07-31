## General

The limit $n \le 13$ makes the $2^n-1$ non-empty node subsets small enough to enumerate directly. Represent a subset by a bitmask, and also represent each node's neighbors by a bitmask. A separate mask marks all nodes whose value is one.

For each non-empty subset, intersect it with the one-node mask and inspect the number of set bits. An odd result cannot contribute and is skipped. For an even subset, begin a graph traversal at its least-significant selected node. The frontier and the reached set are both bitmasks: removing one frontier bit chooses the next node, while intersecting its neighbor mask with the subset prevents the traversal from leaving the induced subgraph. The induced subgraph is connected exactly when the traversal reaches the entire subset.

This tests the two required properties independently and completely. The bit-count test accepts exactly the subsets with an even node-value sum because every value is zero or one. The restricted traversal follows exactly the edges retained by the induced subgraph, so reaching every selected node is equivalent to connectivity. Therefore the counter is incremented for precisely the requested subsets.

## Complexity detail

There are $2^n-1$ non-empty subsets. The parity test and traversal inspect at most $n$ selected nodes per subset, so the total time is $O(n 2^n)$. The adjacency masks and traversal state require $O(n)$ extra space.

## Alternatives and edge cases

- **Adjacency-list traversal:** A conventional DFS or BFS for every subset has the same $O(n 2^n)$ asymptotic bound, but bitmasks make membership checks and frontier updates compact for $n \le 13$.
- **Partition testing:** Checking whether every bipartition of each subset has a crossing edge is correct but can examine $O(3^n)$ subset-partition pairs overall.
- **Single-node subsets:** A single node is connected by definition and contributes exactly when its value is zero.
- **Disconnected original graph:** No special preprocessing is needed; a selected subset contributes only if its own induced subgraph is connected.
- **Even sum without connectivity:** An even value sum alone is insufficient, as a subset spanning disconnected components must still be rejected.
