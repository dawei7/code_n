## General
Given two strings `s1` and `s2`, return *the lowest **ASCII** sum of deleted characters to make two strings equal*, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(\min(m, n))$ — Auxiliary memory allocation bound.
