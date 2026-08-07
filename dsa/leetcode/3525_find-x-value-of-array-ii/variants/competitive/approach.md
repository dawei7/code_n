## General
Algorithm uses two-pointer sliding window iteration. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((n + q log n)k)$ — Operation count bound.
- **Space Complexity**: $O(nk)$ — Auxiliary memory allocation bound.
