## General
Given There exists an undirected tree rooted at node `0` with `n` nodes labeled from `0` to $n - 1$. You are given a 2D **integer** array `edges` of length $n - 1$, where $\text{edges}[i] = [a_{i}, b_{i}]$ indicates that th..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log(C))$ — Operation count bound.
- **Space Complexity**: $O(n log(C))$ — Auxiliary memory allocation bound.
