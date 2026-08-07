## General
Given an integer array `nums` and an integer `k`, return `true` if it is possible to divide this array into `k` non-empty subsets whose sums are all equal, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n \cdot 2^n)$ — Operation count bound.
- **Space Complexity**: $O(2^n)$ — Auxiliary memory allocation bound.
