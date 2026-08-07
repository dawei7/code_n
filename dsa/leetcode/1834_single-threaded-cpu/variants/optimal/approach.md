## General
Given `n`​​​​​​ tasks labeled from `0` to $n - 1$ represented by a 2D integer array `tasks`, where $\text{tasks}[i] = [\text{enqueueTime}_{i}, \text{processingTime}_{i}]$ means that the $i^​​​​​​th$​​​​ task will be availab..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n\log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
