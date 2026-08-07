## General
Given an `m x n` integer matrix `grid`​​​, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(MN\min(M,N))$ — Operation count bound.
- **Space Complexity**: $O(MN)$ — Auxiliary memory allocation bound.
