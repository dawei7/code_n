## General
Given an `m x n` matrix `grid` consisting of characters and a string `pattern`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N + P)$ — Operation count bound.
- **Space Complexity**: $O(N + P)$ — Auxiliary memory allocation bound.
