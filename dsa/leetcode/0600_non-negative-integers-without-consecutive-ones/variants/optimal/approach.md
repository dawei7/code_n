## General
Given a positive integer `n`, return the number of the integers in the range `[0, n]` whose binary representations **do not** contain consecutive ones, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(\log n)$ — Operation count bound.
- **Space Complexity**: $O(\log n)$ — Auxiliary memory allocation bound.
