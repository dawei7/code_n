## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n log n + nV / w)$ — Operation count bound.
- **Space Complexity**: $O(n + V / w)$ — Auxiliary memory allocation bound.
