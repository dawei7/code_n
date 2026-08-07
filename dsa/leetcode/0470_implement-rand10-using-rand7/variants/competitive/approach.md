## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(draws)$ — Operation count bound.
- **Space Complexity**: $O(draws)$ — Auxiliary memory allocation bound.
