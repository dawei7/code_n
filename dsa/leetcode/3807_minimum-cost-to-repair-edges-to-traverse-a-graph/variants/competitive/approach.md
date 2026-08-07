## General
Given an **undirected graph** with `n` nodes labeled from 0 to $n - 1$. The graph consists of `m` edges represented by a 2D integer array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ indicates that there is an e..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O((N + M) log M)$ — Operation count bound.
- **Space Complexity**: $O(N + M)$ — Auxiliary memory allocation bound.
