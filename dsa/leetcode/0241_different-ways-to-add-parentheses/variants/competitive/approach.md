## General
Algorithm uses two-pointer sliding window iteration. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(C_n \cdot n)$ — Operation count bound.
- **Space Complexity**: $O(C_n \cdot n)$ — Auxiliary memory allocation bound.
