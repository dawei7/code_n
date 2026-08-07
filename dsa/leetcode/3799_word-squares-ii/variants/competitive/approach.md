## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(W^3 + A)$ — Operation count bound.
- **Space Complexity**: $O(W + A)$ — Auxiliary memory allocation bound.
