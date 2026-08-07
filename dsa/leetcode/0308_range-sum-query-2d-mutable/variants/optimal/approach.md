## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((mn + q) \log m \log n)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
