## General
Given an `m x n` **0-indexed** 2D array of positive integers `heights` where $\text{heights}[i][j]$ is the height of the person standing at position `(i, j)`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
