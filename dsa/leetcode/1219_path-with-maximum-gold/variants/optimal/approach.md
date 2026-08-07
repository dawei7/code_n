## General
Given In a gold mine `grid` of size `m x n`, each cell in this mine has an integer representing the amount of gold in that cell, `0` if it is empty, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(mn\cdot3^g)$ — Operation count bound.
- **Space Complexity**: $O(g)$ — Auxiliary memory allocation bound.
