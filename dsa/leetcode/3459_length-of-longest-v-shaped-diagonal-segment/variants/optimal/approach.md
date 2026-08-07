## General
Given a 2D integer matrix `grid` of size `n x m`, where each element is either `0`, `1`, or `2`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nm)$ — Operation count bound.
- **Space Complexity**: $O(nm)$ — Auxiliary memory allocation bound.
