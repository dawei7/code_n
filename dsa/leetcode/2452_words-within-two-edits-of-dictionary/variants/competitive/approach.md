## General
Algorithm uses single-pass sequential scanning. Maintains hash set (`set`) for $O(1)$ duplicate check. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(Q D n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
