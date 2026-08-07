## General
Given a **0-indexed** integer array `nums` consisting of `n` non-negative integers, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((n+q)S)$ — Operation count bound.
- **Space Complexity**: $O(n+q)$ — Auxiliary memory allocation bound.
