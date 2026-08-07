## General
Given a positive integer **0-indexed** array `nums`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + U * 2^P)$ — Operation count bound.
- **Space Complexity**: $O(2^P)$ — Auxiliary memory allocation bound.
