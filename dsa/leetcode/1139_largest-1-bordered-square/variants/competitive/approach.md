## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(mnq)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
