## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(VT+T^2\log T)$ — Operation count bound.
- **Space Complexity**: $O(T^2)$ — Auxiliary memory allocation bound.
