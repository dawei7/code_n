## General
Given an integer `n` representing the number of tasks in a project, numbered from 0 to $n - 1$. These tasks are connected as an undirected** tree**. This is represented by a 2D integer array `edges` of length $n - 1$, where..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
