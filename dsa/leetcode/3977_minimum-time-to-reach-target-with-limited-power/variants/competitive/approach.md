## General
Given a **directed** weighted graph with `n` nodes labeled from 0 to $n - 1$, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(P(n + m) log(nP))$ — Operation count bound.
- **Space Complexity**: $O(nP + m)$ — Auxiliary memory allocation bound.
