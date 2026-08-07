## General
Given an `m x n` integer matrix `grid` where each entry is only `0` or `1`, return *the number of **corner rectangles***, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(mn \min(m,n))$ — Operation count bound.
- **Space Complexity**: $O(\min(m,n)^2)$ — Auxiliary memory allocation bound.
