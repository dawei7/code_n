## General
Given a 2D integer array `occupiedIntervals`, where $\text{occupiedIntervals}[i] = [\text{start}_{i}, \text{end}_{i}]$ represents a time interval during which you are occupied. Each interval starts at $\text{start}_{i}$ and..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
