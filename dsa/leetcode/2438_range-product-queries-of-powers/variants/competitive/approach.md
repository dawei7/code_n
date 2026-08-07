## General
Algorithm uses two-pointer sliding window iteration. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(log n + q)$ — Operation count bound.
- **Space Complexity**: $O(log n + q)$ — Auxiliary memory allocation bound.
