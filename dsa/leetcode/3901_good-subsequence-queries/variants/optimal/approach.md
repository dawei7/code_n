## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M log log M + (N + Q)(log N + log M))$ — Operation count bound.
- **Space Complexity**: $O(N + M)$ — Auxiliary memory allocation bound.
