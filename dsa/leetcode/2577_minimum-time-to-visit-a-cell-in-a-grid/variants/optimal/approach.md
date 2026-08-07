## General
Given a `m x n` matrix `grid` consisting of **non-negative** integers where $\text{grid}[row][col]$ represents the **minimum** time required to be able to visit the cell `(row, col)`, which means you can visit the cell `(ro..., the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(mn log(mn))$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
