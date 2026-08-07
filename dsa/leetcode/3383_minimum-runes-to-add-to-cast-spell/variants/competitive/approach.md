## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + m)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
