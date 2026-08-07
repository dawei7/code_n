## General
Given a **0-indexed** binary matrix `grid`. In one operation, you can flip any `1` in `grid` to be `0`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(E sqrt V)$ — Operation count bound.
- **Space Complexity**: $O(V + E)$ — Auxiliary memory allocation bound.
