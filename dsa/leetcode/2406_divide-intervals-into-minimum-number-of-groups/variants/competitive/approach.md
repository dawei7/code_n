## General
Given a 2D integer array `intervals` where $\text{intervals}[i] = [\text{left}_{i}, \text{right}_{i}]$ represents the **inclusive** interval $[\text{left}_{i}, \text{right}_{i}]$, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
