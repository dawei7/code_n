## General
Given There is an undirected tree with `n` nodes labeled from `0` to $n - 1$. You are given the integer `n` and a 2D integer array `edges` of length $n - 1$, where $\text{edges}[i] = [a_{i}, b_{i}]$ indicates that there is ..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log S)$ — Operation count bound.
- **Space Complexity**: $O(n log S)$ — Auxiliary memory allocation bound.
