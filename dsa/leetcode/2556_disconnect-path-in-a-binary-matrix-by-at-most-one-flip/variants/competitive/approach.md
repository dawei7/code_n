## General
Given a **0-indexed** `m x n` **binary** matrix `grid`. You can move from a cell `(row, col)` to any of the cells $(row + 1, col)$ or $(row, col + 1)$ that has the value `1`. The matrix is **disconnected** if there is no pa..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(m + n)$ — Auxiliary memory allocation bound.
