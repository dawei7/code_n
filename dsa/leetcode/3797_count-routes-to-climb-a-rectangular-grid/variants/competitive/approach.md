## General
Given a string array `grid` of size `n`, where each string $\text{grid}[i]$ has length `m`. The character $\text{grid}[i][j]$ is one of the following symbols:, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(NM)$ — Operation count bound.
- **Space Complexity**: $O(M)$ — Auxiliary memory allocation bound.
