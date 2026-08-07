## General
Given two strings `s` and `t`, the algorithm solves **Longest Common Prefix After at Most One Removal** directly. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(min(n, m))$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
