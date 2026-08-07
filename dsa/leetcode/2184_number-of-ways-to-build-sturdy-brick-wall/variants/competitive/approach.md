## General
Algorithm uses depth-first search recursion. Maintains hash set (`set`) for $O(1)$ duplicate check, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(R^2 + hE)$ — Operation count bound.
- **Space Complexity**: $O(R^2)$ — Auxiliary memory allocation bound.
