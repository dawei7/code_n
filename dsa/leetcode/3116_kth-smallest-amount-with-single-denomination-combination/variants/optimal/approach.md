## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(2^m (m + log U))$ — Operation count bound.
- **Space Complexity**: $O(2^m + m)$ — Auxiliary memory allocation bound.
