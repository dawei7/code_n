## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(P\sqrt{A})$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
