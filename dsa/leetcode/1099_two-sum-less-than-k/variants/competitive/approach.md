## General
Given an array `nums` of integers and integer `k`, return the maximum `sum` such that there exists `i < j` with $\text{nums}[i] + \text{nums}[j] = sum$ and `sum < k`. If no `i`, `j` exist satisfying this equation, return `-1`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
