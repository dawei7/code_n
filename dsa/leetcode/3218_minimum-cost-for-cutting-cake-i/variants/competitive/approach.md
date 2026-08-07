## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(m log m + n log n)$ — Operation count bound.
- **Space Complexity**: $O(m + n)$ — Auxiliary memory allocation bound.
