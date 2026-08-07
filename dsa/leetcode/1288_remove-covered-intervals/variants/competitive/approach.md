## General
Given an array `intervals` where $\text{intervals}[i] = [l_{i}, r_{i}]$ represent the interval $[l_{i}, r_{i})$, remove all intervals that are covered by another interval in the list, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
