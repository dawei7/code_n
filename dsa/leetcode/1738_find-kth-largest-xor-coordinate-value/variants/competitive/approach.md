## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(C\log k)$ — Operation count bound.
- **Space Complexity**: $O(n+k)$ — Auxiliary memory allocation bound.
