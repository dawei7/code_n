## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(2^D)$ — Operation count bound.
- **Space Complexity**: $O(2^D)$ — Auxiliary memory allocation bound.
