## General
Given two integer arrays, `nums1` and `nums2`, both of length `n`, along with a positive integer `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
