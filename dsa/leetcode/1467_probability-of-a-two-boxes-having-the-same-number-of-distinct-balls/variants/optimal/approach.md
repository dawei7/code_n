## General
Given `2n` balls of `k` distinct colors. You will be given an integer array `balls` of size `k` where $\text{balls}[i]$ is the number of balls of color `i`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(K^2nB)$ — Operation count bound.
- **Space Complexity**: $O(Kn)$ — Auxiliary memory allocation bound.
