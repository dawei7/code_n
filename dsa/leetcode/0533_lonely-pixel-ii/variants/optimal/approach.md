## General
Given an `m x n` `picture` consisting of black `'B'` and white `'W'` pixels and an integer target, return *the number of **black** lonely pixels*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(rows \cdot cols)$ — Operation count bound.
- **Space Complexity**: $O(rows \cdot cols)$ — Auxiliary memory allocation bound.
