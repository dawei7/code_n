## General
Given a rectangle of size `n` x `m`, return *the minimum number of integer-sided squares that tile the rectangle*, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O\left(wh(h+1)^w\right)$ — Operation count bound.
- **Space Complexity**: $O\left((h+1)^w\right)$ — Auxiliary memory allocation bound.
