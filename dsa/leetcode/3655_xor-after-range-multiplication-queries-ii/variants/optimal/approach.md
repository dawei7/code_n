## General
Algorithm uses two-pointer sliding window iteration. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((n + q) sqrt(n) + q log MOD)$ — Operation count bound.
- **Space Complexity**: $O(n + q)$ — Auxiliary memory allocation bound.
