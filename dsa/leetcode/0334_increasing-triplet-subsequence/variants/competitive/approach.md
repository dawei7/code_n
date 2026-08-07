## General
Given an integer array `nums`, return `true`* if there exists a triple of indices *`(i, j, k)`* such that *`i < j < k`* and *$\text{nums}[i] < \text{nums}[j] < \text{nums}[k]$. If no such indices exists, return `false`, the algorithm executes a single-pass linear scan through input elements. Edge case handling: uses infinity sentinels for safe boundary initialization.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
