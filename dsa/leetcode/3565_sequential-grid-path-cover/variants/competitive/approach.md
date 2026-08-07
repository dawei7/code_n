## General
Given a 2D array `grid` of size `m x n`, and an integer `k`. There are `k` cells in `grid` containing the values from 1 to `k` **exactly once**, and the rest of the cells have a value 0, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(V * 3^V)$ — Operation count bound.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.
