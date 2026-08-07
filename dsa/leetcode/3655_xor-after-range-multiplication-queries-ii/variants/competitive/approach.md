## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((n + q) sqrt(n) + q log MOD)$ — Operation count bound.
- **Space Complexity**: $O(n + q)$ — Auxiliary memory allocation bound.
