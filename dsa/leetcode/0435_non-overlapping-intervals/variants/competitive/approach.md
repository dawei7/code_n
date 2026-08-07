## General
Given an array of intervals `intervals` where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$, return *the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping*, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
