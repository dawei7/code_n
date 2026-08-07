## General
Given an integer `n` which is the length of a **0-indexed** array `nums`, and a **0-indexed** 2D-array `ranges`, which is a list of sub-ranges of `nums` (sub-ranges may **overlap**), the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(m log m)$ — Operation count bound.
- **Space Complexity**: $O(m)$ — Auxiliary memory allocation bound.
