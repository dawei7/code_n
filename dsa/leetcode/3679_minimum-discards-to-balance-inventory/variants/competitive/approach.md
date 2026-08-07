## General
Given two integers `w` and `m`, and an integer array `arrivals`, where $\text{arrivals}[i]$ is the type of item arriving on day `i` (days are **1-indexed**), the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
