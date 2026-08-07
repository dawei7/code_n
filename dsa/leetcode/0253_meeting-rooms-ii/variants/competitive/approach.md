## General
Given an array of meeting time intervals `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$, return *the minimum number of conference rooms required*, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
