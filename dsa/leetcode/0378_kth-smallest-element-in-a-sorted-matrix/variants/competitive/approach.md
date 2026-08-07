## General
Given an `n x n` `matrix` where each of the rows and columns is sorted in ascending order, return *the* $$k^{\text{th}}$$ *smallest element in the matrix*, the algorithm solves **Kth Smallest Element in a Sorted Matrix** directly. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n \log R)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
