## General
Algorithm uses single-pass sequential scanning. Maintains hash set (`set`) for $O(1)$ duplicate check, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
