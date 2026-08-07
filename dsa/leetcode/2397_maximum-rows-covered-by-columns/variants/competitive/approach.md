## General
Given an `m x n` binary matrix `matrix` and an integer `numSelect`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(mn + (m + k) C(n,k))$ — Operation count bound.
- **Space Complexity**: $O(m)$ — Auxiliary memory allocation bound.
