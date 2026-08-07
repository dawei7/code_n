## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n^2 * log M)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
