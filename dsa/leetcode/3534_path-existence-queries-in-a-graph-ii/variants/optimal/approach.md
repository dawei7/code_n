## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((n + Q) * log n)$ — Operation count bound.
- **Space Complexity**: $O(n * log n)$ — Auxiliary memory allocation bound.
