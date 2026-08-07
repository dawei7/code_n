## General
Given two integer arrays `nums1` and `nums2` of length `n`, count the pairs of indices `(i, j)` such that `i < j` and $\text{nums1}[i] + \text{nums1}[j] > \text{nums2}[i] + \text{nums2}[j]$, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window.

## Complexity detail
- **Time Complexity**: $O(N\log N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
