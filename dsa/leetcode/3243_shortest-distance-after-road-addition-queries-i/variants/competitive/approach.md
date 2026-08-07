## General
Given an integer `n` and a 2D integer array `queries`, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(q(n+q))$ — Operation count bound.
- **Space Complexity**: $O(n+q)$ — Auxiliary memory allocation bound.
