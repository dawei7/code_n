## General
Given an `m x n` integers `matrix`, return *the length of the longest increasing path in *`matrix`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
