## General
Given an integer array `nums` and a **positive** integer `k`. You can choose any **subsequence** of the array and sum all of its elements together, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(n log n + k log k)$ — Operation count bound.
- **Space Complexity**: $O(n + k)$ — Auxiliary memory allocation bound.
