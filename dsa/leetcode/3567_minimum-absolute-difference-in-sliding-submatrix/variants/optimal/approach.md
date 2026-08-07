## General
Given an `m x n` integer matrix `grid` and an integer `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(R C k^2 log k)$ — Operation count bound.
- **Space Complexity**: $O(k^2 + R C)$ — Auxiliary memory allocation bound.
