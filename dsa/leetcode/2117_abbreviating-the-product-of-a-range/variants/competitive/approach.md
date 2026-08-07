## General
Given two positive integers `left` and `right` with $left \le right$. Calculate the **product** of all integers in the **inclusive** range `[left, right]`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N log R)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
