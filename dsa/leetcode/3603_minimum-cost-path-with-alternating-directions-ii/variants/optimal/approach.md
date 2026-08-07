## General
Given two integers `m` and `n` representing the number of rows and columns of a grid, respectively, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(m n)$ — Operation count bound.
- **Space Complexity**: $O(min(m, n))$ — Auxiliary memory allocation bound.
