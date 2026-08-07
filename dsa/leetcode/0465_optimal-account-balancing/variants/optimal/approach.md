## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n + k!)$ — Operation count bound.
- **Space Complexity**: $O(p + k^2)$ — Auxiliary memory allocation bound.
