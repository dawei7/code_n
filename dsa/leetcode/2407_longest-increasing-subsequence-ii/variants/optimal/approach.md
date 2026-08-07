## General
Given an integer array `nums` and an integer `k`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log M)$ — Operation count bound.
- **Space Complexity**: $O(M)$ — Auxiliary memory allocation bound.
