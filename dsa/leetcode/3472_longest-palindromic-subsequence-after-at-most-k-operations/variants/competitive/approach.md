## General
Given a string `s` and an integer `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2 * k)$ — Operation count bound.
- **Space Complexity**: $O(n * k)$ — Auxiliary memory allocation bound.
