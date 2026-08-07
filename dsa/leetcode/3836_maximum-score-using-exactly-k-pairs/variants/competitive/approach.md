## General
Given two integer arrays `nums1` and `nums2` of lengths `n` and `m` respectively, and an integer `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N M K)$ — Operation count bound.
- **Space Complexity**: $O(K min(N,M))$ — Auxiliary memory allocation bound.
