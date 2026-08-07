## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((N + Q) log N)$ — Operation count bound.
- **Space Complexity**: $O(N log N)$ — Auxiliary memory allocation bound.
