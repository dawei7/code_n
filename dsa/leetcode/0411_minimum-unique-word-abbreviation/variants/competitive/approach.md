## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O((d + m)2^p)$ — Operation count bound.
- **Space Complexity**: $O(d + 2^p)$ — Auxiliary memory allocation bound.
