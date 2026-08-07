## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n \cdot 2^n)$ — Operation count bound.
- **Space Complexity**: $O(2^n)$ — Auxiliary memory allocation bound.
