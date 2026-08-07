## General
Algorithm uses two-pointer sliding window iteration. Maintains hash set (`set`) for $O(1)$ duplicate check, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n\log M)$ — Operation count bound.
- **Space Complexity**: $O(\log M)$ — Auxiliary memory allocation bound.
