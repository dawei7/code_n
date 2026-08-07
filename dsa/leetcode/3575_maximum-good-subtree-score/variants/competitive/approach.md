## General
Algorithm uses depth-first search recursion. Maintains hash map lookup (`dict`) for $O(1)$ average speed, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n * 3^D)$ — Operation count bound.
- **Space Complexity**: $O(n * 2^D)$ — Auxiliary memory allocation bound.
