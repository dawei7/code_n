## General
Given an integer array `nums`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M\log\log M+n\log M)$ — Operation count bound.
- **Space Complexity**: $O(M+n)$ — Auxiliary memory allocation bound.
