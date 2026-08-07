## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(m * 2^m + n)$ — Operation count bound.
- **Space Complexity**: $O(2^m)$ — Auxiliary memory allocation bound.
