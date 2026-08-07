## General
Given an integer `n` and a 2D array `requirements`, where $\text{requirements}[i] = [\text{end}_{i}, \text{cnt}_{i}]$ represents the end index and the **inversion** count of each requirement, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nC)$ — Operation count bound.
- **Space Complexity**: $O(n + C)$ — Auxiliary memory allocation bound.
