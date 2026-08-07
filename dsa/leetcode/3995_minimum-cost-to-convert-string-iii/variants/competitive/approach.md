## General
Given two strings, `source` and `target`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nRL)$ — Operation count bound.
- **Space Complexity**: $O(n+R)$ — Auxiliary memory allocation bound.
