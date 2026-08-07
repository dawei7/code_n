## General
Given an integer array `nums` of length `n` and an integer `p`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M log log M + (N + Q)(log N + log M))$ — Operation count bound.
- **Space Complexity**: $O(N + M)$ — Auxiliary memory allocation bound.
