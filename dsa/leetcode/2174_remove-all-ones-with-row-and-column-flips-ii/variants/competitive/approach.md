## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(k 2^k)$ — Operation count bound.
- **Space Complexity**: $O(2^k)$ — Auxiliary memory allocation bound.
