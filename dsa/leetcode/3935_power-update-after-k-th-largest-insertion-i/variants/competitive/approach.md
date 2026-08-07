## General
Given an integer array `nums` and an integer `p`, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((N + Q) log(N + Q) + Q log V)$ — Operation count bound.
- **Space Complexity**: $O(N + Q)$ — Auxiliary memory allocation bound.
