## General
Given There is a tree (i.e., a connected, undirected graph that has no cycles) consisting of `n` nodes numbered from `0` to $n - 1$ and exactly $n - 1$ edges. Each node has a value associated with it, and the **root** of th..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
