## General
Algorithm uses depth-first search recursion. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(K^2 \cdot 2^K)$ — Operation count bound.
- **Space Complexity**: $O(K \cdot 2^K)$ — Auxiliary memory allocation bound.
