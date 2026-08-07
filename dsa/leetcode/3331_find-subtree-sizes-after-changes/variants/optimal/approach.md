## General
Given a tree rooted at node 0 that consists of `n` nodes numbered from `0` to $n - 1$. The tree is represented by an array `parent` of size `n`, where $\text{parent}[i]$ is the parent of node `i`. Since node 0 is the root, ..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
