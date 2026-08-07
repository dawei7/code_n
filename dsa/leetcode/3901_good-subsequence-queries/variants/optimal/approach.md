## General
Given an integer array `nums` of length `n` and an integer `p`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M log log M + (N + Q)(log N + log M))$ — Operation count bound.
- **Space Complexity**: $O(N + M)$ — Auxiliary memory allocation bound.
