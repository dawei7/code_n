## General
Given three integers `n`, `x`, and `y`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n min(n, x))$ — Operation count bound.
- **Space Complexity**: $O(min(n, x))$ — Auxiliary memory allocation bound.
