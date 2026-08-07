## General
Given an integer `n` representing the number of tasks in a project, numbered from 0 to $n - 1$. These tasks are connected as a **tree** rooted at task 0. This is represented by a 2D integer array `edges` of length $n - 1$, ..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
