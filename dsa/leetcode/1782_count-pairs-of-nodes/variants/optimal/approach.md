## General
Given an undirected graph defined by an integer `n`, the number of nodes, and a 2D integer array `edges`, the edges in the graph, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates that there is an **undirected** edge betwe..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(E + n\log n + Q(n + P))$ — Operation count bound.
- **Space Complexity**: $O(n + P)$ — Auxiliary memory allocation bound.
