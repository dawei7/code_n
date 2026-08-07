## General
Given an `m x n` integer matrix `grid`​​​, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(MN\min(M,N))$ — Operation count bound.
- **Space Complexity**: $O(MN)$ — Auxiliary memory allocation bound.
