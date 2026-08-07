## General
Given an integer array `nums` of length `n`, where `nums` is a permutation of the integers in the range `[0, n - 1]`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(Pqn)$ — Operation count bound.
- **Space Complexity**: $O(Pn)$ — Auxiliary memory allocation bound.
