## General
Given Android devices have a special lock screen with a `3 x 3` grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's en..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(K^2 \cdot 2^K)$ — Operation count bound.
- **Space Complexity**: $O(K \cdot 2^K)$ — Auxiliary memory allocation bound.
