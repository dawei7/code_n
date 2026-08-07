## General
Given You have `n`  `tiles`, where each tile has one letter $\text{tiles}[i]$ printed on it, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(DM)$ — Operation count bound.
- **Space Complexity**: $O(M+n)$ — Auxiliary memory allocation bound.
