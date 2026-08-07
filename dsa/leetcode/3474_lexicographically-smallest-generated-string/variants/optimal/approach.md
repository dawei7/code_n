## General
Given two strings, `str1` and `str2`, of lengths `n` and `m`, respectively, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n + m)m)$ — Operation count bound.
- **Space Complexity**: $O((n + m)m)$ — Auxiliary memory allocation bound.
