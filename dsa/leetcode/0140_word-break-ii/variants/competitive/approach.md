## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(S + n + R)$ — Operation count bound.
- **Space Complexity**: $O(D + n + R)$ — Auxiliary memory allocation bound.
