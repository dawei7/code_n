## General
Given an integer array `nums` of length `n` and a 2D integer array `queries` of size `q`, where $\text{queries}[i] = [l_{i}, r_{i}, k_{i}, v_{i}]$, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + U)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
