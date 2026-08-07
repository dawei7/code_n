## General
Given a **weighted** tree consisting of `n` nodes numbered from `0` to $n - 1$, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
