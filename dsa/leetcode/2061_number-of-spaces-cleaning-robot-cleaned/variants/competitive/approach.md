## General
Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
