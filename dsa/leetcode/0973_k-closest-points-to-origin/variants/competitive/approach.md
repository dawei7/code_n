## General
Given an array of `points` where $\text{points}[i] = [x_{i}, y_{i}]$ represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(K)$ — Auxiliary memory allocation bound.
