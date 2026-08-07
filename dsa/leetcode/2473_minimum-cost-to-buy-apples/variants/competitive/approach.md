## General
Given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a **2D** array `roads`, where $\text{roads}[i] = [a_{i}, b_{i}, \text{cost}_{i}]$ indicates that there is a **bidirectional *..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O((n + m) log n)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
