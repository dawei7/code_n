## General
Given an `m x n` integer matrix `grid` and an array `queries` of size `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(m n log(m n) + k log k)$ — Operation count bound.
- **Space Complexity**: $O(m n + k)$ — Auxiliary memory allocation bound.
