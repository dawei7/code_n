## General
Given an integer array `nums`, return *all the different possible non-decreasing subsequences of the given array with at least two elements*. You may return the answer in **any order**, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n \cdot 2^n)$ — Operation count bound.
- **Space Complexity**: $O(n \cdot 2^n)$ — Auxiliary memory allocation bound.
