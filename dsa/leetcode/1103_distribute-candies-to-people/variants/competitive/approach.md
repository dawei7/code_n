## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(P)$ — Operation count bound.
- **Space Complexity**: $O(P)$ — Auxiliary memory allocation bound.
