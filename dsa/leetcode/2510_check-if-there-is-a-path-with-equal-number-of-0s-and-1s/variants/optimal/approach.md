## General
Given a **0-indexed** `m x n` **binary** matrix `grid`. You can move from a cell `(row, col)` to any of the cells $(row + 1, col)$ or $(row, col + 1)$, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(rc(r + c))$ — Operation count bound.
- **Space Complexity**: $O(c(r + c))$ — Auxiliary memory allocation bound.
