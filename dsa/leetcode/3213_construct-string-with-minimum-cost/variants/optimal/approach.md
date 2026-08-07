## General
Given a string `target`, an array of strings `words`, and an integer array `costs`, both arrays of the same length, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N D + S)$ — Operation count bound.
- **Space Complexity**: $O(N + S)$ — Auxiliary memory allocation bound.
