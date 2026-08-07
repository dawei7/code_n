## General
Given an `m x n` integer matrix `grid` and an integer `k`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(R C k^2 log k)$ — Operation count bound.
- **Space Complexity**: $O(k^2 + R C)$ — Auxiliary memory allocation bound.
