## General
Given an integer array `nums`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n + B * 2^B)$ — Operation count bound.
- **Space Complexity**: $O(2^B)$ — Auxiliary memory allocation bound.
