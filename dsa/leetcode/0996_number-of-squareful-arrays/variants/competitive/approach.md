## General
Given An array is **squareful** if the sum of every pair of adjacent elements is a **perfect square**, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(N!)$ — Operation count bound.
- **Space Complexity**: $O(N+U^2)$ — Auxiliary memory allocation bound.
