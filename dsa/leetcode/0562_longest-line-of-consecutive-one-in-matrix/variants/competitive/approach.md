## General
Given an `m x n` binary matrix `mat`, return *the length of the longest line of consecutive one in the matrix*, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(rc)$ — Operation count bound.
- **Space Complexity**: $O(c)$ — Auxiliary memory allocation bound.
