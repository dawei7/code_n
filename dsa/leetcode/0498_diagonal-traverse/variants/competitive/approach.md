## General
Given an `m x n` matrix `mat`, return *an array of all the elements of the array in a diagonal order*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(rows \cdot cols)$ — Operation count bound.
- **Space Complexity**: $O(rows \cdot cols)$ — Auxiliary memory allocation bound.
