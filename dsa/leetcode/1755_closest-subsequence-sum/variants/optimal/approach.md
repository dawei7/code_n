## General
Given an integer array `nums` and an integer `goal`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(n2^{n/2})$ — Operation count bound.
- **Space Complexity**: $O(2^{n/2})$ — Auxiliary memory allocation bound.
