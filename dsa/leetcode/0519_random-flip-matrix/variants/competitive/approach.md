## General
Given There is an `m x n` binary grid `matrix` with all the values set `0` initially. Design an algorithm to randomly pick an index `(i, j)` where $\text{matrix}[i][j] = 0$ and flips it to `1`. All the indices `(i, j)` wher..., the algorithm solves **Random Flip Matrix** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(q)$ — Operation count bound.
- **Space Complexity**: $O(f)$ — Auxiliary memory allocation bound.
