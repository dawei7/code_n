## General
Given an undirected tree rooted at node 0 with `n` nodes numbered from 0 to $n - 1$, represented by an array `parent` where $\text{parent}[i]$ is the parent of node `i`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((n + q) log n)$ — Operation count bound.
- **Space Complexity**: $O(n log n)$ — Auxiliary memory allocation bound.
