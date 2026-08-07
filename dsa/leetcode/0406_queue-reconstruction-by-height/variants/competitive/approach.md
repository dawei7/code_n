## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
