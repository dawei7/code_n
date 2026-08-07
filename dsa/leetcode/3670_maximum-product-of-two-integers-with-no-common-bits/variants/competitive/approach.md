## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n + B * 2^B)$ — Operation count bound.
- **Space Complexity**: $O(2^B)$ — Auxiliary memory allocation bound.
