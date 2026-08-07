## General
Given a 2D integer array `grid` of size $m * n$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
