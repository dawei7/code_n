## General
Given an integer array `nums` and an integer `k`. You can partition the array into **at most** `k` non-empty adjacent subarrays. The **score** of a partition is the sum of the averages of each subarray, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches.

## Complexity detail
- **Time Complexity**: $O(k \cdot n^2)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
