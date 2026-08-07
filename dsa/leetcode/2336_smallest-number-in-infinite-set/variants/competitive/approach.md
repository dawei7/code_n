## General
Given You have a set which contains all positive integers `[1, 2, 3, 4, 5, ...]`, the algorithm solves **Smallest Number in Infinite Set** directly. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(q log q)$ — Operation count bound.
- **Space Complexity**: $O(q)$ — Auxiliary memory allocation bound.
