## General
Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(d^2)$ — Operation count bound.
- **Space Complexity**: $O(d^2)$ — Auxiliary memory allocation bound.
