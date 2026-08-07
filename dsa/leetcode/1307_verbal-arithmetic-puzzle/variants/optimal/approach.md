## General
Given an equation, represented by `words` on the left side and the `result` on the right side, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(10!)$ — Operation count bound.
- **Space Complexity**: $O(U+L)$ — Auxiliary memory allocation bound.
