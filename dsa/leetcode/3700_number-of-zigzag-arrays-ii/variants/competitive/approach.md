## General
Algorithm uses two-pointer sliding window iteration. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m^3 log n)$ — Operation count bound.
- **Space Complexity**: $O(m^2)$ — Auxiliary memory allocation bound.
