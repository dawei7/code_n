## General
Given an integer array `nums` of length `n` and an integer `k`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n + k log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
