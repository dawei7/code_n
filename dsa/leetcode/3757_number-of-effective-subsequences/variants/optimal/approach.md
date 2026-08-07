## General
Given an integer array `nums`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nb + b 2^b)$ — Operation count bound.
- **Space Complexity**: $O(n + 2^b)$ — Auxiliary memory allocation bound.
