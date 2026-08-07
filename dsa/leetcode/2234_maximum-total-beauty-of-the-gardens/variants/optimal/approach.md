## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log n + n log target)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
