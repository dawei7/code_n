## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M\log\log M+n\log M)$ — Operation count bound.
- **Space Complexity**: $O(M+n)$ — Auxiliary memory allocation bound.
