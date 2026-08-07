## General
Given a 2D array `intervals`, where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$ represents the start and the end of interval `i`. You are also given an integer `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
