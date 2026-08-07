## General
Given a **1-indexed** `m x n` integer matrix `mat`, you can select any cell in the matrix as your **starting cell**, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(m*n*log(m*n))$ — Operation count bound.
- **Space Complexity**: $O(m*n)$ — Auxiliary memory allocation bound.
