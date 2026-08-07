## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m^2 2^m)$ — Operation count bound.
- **Space Complexity**: $O(m^2 + 2^m)$ — Auxiliary memory allocation bound.
