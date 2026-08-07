## General
Given two **positive** integers `n` and `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(p n log n)$ — Operation count bound.
- **Space Complexity**: $O(pn)$ — Auxiliary memory allocation bound.
