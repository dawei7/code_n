## General
Given two positive integers `m` and `n` which are the height and width of a **0-indexed** 2D-array `board`, a pair of positive integers `(r, c)` which is the starting position of the knight on the board, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(8^(mn))$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
