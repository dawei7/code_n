## General
Given a positive integer `n` and a 2D integer array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O((N + E) log N)$ — Operation count bound.
- **Space Complexity**: $O(N + E)$ — Auxiliary memory allocation bound.
