## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(M\log\log M+N\log M+N\log N)$ — Operation count bound.
- **Space Complexity**: $O(M)$ — Auxiliary memory allocation bound.
