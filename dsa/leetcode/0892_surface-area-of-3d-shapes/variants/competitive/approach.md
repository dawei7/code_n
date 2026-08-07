## General
Given an `n x n` `grid` where you have placed some `1 x 1 x 1` cubes. Each value $v = \text{grid}[i][j]$ represents a tower of `v` cubes placed on top of cell `(i, j)`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
