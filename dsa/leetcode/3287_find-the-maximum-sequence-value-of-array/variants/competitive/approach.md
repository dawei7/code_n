## General
Algorithm uses two-pointer sliding window iteration. Maintains hash set (`set`) for $O(1)$ duplicate check, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n(kB + B^2))$ — Operation count bound.
- **Space Complexity**: $O((n + k)B)$ — Auxiliary memory allocation bound.
