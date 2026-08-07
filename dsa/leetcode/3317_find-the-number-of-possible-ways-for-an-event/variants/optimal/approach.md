## General
Given three integers `n`, `x`, and `y`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n min(n, x))$ — Operation count bound.
- **Space Complexity**: $O(min(n, x))$ — Auxiliary memory allocation bound.
