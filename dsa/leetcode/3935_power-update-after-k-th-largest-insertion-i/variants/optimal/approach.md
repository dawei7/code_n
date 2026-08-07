## General
Given an integer array `nums` and an integer `p`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((N + Q) log(N + Q) + Q log V)$ — Operation count bound.
- **Space Complexity**: $O(N + Q)$ — Auxiliary memory allocation bound.
