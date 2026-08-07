## General
Given a `m x n` 2D array `board` representing a chessboard, where $\text{board}[i][j]$ represents the **value** of the cell `(i, j)`, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(m+n)$ — Auxiliary memory allocation bound.
