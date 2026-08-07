## General
Given an integer array `nums` and two integers `k` and `mul`, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n log(k + 1))$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
