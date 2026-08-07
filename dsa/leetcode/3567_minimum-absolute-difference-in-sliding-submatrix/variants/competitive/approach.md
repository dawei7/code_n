## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(R C k^2 log k)$ — Operation count bound.
- **Space Complexity**: $O(k^2 + R C)$ — Auxiliary memory allocation bound.
