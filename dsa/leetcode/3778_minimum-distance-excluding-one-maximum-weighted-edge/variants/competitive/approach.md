## General
Given a positive integer `n` and a 2D integer array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((N + E) log N)$ — Operation count bound.
- **Space Complexity**: $O(N + E)$ — Auxiliary memory allocation bound.
