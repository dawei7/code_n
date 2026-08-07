## General
Given an integer `n` and an integer array `prices` of length `n`, where $\text{prices}[i]$ is the price of apples at shop `i`, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(n log n (n + m))$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
