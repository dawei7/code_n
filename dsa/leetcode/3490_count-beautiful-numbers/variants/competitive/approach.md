## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(D^4)$ — Operation count bound.
- **Space Complexity**: $O(D^3)$ — Auxiliary memory allocation bound.
