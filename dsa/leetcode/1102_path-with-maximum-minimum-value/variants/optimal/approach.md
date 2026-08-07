## General
Given an `m x n` integer matrix `grid`, return *the maximum **score** of a path starting at *`(0, 0)`* and ending at *$(m - 1, n - 1)$ moving in the 4 cardinal directions, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(V \log V)$ — Operation count bound.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.
