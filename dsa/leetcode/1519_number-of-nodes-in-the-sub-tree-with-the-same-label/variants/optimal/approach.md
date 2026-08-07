## General
Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of `n` nodes numbered from `0` to $n - 1$ and exactly $n - 1$ `edges`. The **root** of the tree is the node `0`, and each node of the tree has ..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
