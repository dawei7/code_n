## General
Algorithm uses breadth-first search queue level traversal. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n log n + n d^3)$ — Operation count bound.
- **Space Complexity**: $O(n + d^2)$ — Auxiliary memory allocation bound.
