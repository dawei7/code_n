## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(b log b + p log p)$ — Operation count bound.
- **Space Complexity**: $O(b + p)$ — Auxiliary memory allocation bound.
