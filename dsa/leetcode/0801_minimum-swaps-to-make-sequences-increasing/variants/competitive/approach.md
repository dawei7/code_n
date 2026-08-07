## General
Given two integer arrays of the same length `nums1` and `nums2`. In one operation, you are allowed to swap $\text{nums1}[i]$ with $\text{nums2}[i]$, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
