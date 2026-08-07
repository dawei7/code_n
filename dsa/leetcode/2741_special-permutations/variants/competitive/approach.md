## General
Given a **0-indexed** integer array `nums` containing `n` **distinct** positive integers. A permutation of `nums` is called special if:, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n^2 2^n)$ — Operation count bound.
- **Space Complexity**: $O(n 2^n)$ — Auxiliary memory allocation bound.
