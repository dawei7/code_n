## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(numRows^2)$ — Operation count bound.
- **Space Complexity**: $O(numRows^2)$ — Auxiliary memory allocation bound.
