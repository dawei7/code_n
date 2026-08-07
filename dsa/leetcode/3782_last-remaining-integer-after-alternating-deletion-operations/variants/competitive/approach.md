## General
Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(log N)$ — Operation count bound.
- **Space Complexity**: $O(log N)$ — Auxiliary memory allocation bound.
