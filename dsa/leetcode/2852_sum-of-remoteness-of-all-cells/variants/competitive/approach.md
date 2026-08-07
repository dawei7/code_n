## General
Given a **0-indexed** matrix `grid` of order $n * n$. Each cell in this matrix has a value $\text{grid}[i][j]$, which is either a **positive** integer or `-1` representing a blocked cell, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
