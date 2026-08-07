## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(C E + C + Q)$ — Operation count bound.
- **Space Complexity**: $O(C^2 + E)$ — Auxiliary memory allocation bound.
