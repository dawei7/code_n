## General
Given a string `s` and a positive integer `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N + sqrt(K))$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
