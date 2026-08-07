## General
Given two arrays, `nums` and `target`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m 2^m + n 3^m)$ — Operation count bound.
- **Space Complexity**: $O(2^m)$ — Auxiliary memory allocation bound.
