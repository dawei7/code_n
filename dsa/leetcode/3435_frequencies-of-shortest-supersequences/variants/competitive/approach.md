## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(W + 2^C C^2)$ — Operation count bound.
- **Space Complexity**: $O(C)$ — Auxiliary memory allocation bound.
