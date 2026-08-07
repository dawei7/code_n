## General
Given a positive integer `n` representing the number of nodes of a **Directed Acyclic Graph** (DAG). The nodes are numbered from `0` to $n - 1$ (**inclusive**), the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n^2 + nm)$ — Operation count bound.
- **Space Complexity**: $O(n^2 + m)$ — Auxiliary memory allocation bound.
