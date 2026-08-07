## General
Given an integer array `nums` consisting of $2 * n$ integers, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m)$ — Operation count bound.
- **Space Complexity**: $O(v)$ — Auxiliary memory allocation bound.
