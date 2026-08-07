## General
Given an integer `n` and an integer array `prices` of length `n`, where $\text{prices}[i]$ is the price of apples at shop `i`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(n log n (n + m))$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
