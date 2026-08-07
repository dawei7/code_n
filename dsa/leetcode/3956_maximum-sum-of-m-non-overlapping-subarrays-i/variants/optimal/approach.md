## General
Given an integer array `nums` of length `n`, and three integers `m`, `l`, and `r`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(m * n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
