## General
Given three strings `word1`, `word2`, and `target`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(tnm)$ — Operation count bound.
- **Space Complexity**: $O(nm)$ — Auxiliary memory allocation bound.
