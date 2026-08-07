## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nb + b 2^b)$ — Operation count bound.
- **Space Complexity**: $O(n + 2^b)$ — Auxiliary memory allocation bound.
