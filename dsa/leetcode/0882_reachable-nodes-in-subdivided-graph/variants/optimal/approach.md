## General
Given an undirected graph (the **"original graph"**) with `n` nodes labeled from `0` to $n - 1$. You decide to **subdivide** each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include the walrus operator (`:=`) for inline assignment and evaluation.

## Complexity detail
- **Time Complexity**: $O((n+m)\log n)$ — Operation count bound.
- **Space Complexity**: $O(n+m)$ — Auxiliary memory allocation bound.
