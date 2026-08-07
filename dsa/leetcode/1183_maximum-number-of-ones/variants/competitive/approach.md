## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(s^2\log s)$ — Operation count bound.
- **Space Complexity**: $O(s^2)$ — Auxiliary memory allocation bound.
