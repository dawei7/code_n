## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(M^2Q+M2^M)$ — Operation count bound.
- **Space Complexity**: $O(M^2+2^M)$ — Auxiliary memory allocation bound.
