## General
Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(k)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
