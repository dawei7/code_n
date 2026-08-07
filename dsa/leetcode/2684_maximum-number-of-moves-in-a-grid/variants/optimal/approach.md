## General
Given a **0-indexed** `m x n` matrix `grid` consisting of **positive** integers, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(m)$ — Auxiliary memory allocation bound.
