## General
Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(B)$ — Operation count bound.
- **Space Complexity**: $O(B)$ — Auxiliary memory allocation bound.
