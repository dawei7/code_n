## General
Given two **positive** integers `n` and `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(p n log n)$ — Operation count bound.
- **Space Complexity**: $O(pn)$ — Auxiliary memory allocation bound.
