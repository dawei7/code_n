## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n+f3^m)$ — Operation count bound.
- **Space Complexity**: $O(2^m+f)$ — Auxiliary memory allocation bound.
