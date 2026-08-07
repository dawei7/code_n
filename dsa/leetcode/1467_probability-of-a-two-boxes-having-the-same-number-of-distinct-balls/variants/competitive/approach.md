## General
Given `2n` balls of `k` distinct colors. You will be given an integer array `balls` of size `k` where $\text{balls}[i]$ is the number of balls of color `i`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(K^2nB)$ — Operation count bound.
- **Space Complexity**: $O(Kn)$ — Auxiliary memory allocation bound.
