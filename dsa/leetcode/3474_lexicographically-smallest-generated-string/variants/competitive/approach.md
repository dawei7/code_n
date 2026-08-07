## General
Given two strings, `str1` and `str2`, of lengths `n` and `m`, respectively, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n + m)m)$ — Operation count bound.
- **Space Complexity**: $O((n + m)m)$ — Auxiliary memory allocation bound.
