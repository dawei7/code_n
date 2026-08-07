## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n+\sigma\log f)$ — Operation count bound.
- **Space Complexity**: $O(\sigma)$ — Auxiliary memory allocation bound.
