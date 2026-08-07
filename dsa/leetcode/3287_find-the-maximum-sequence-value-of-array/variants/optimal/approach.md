## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n(kB + B^2))$ — Operation count bound.
- **Space Complexity**: $O((n + k)B)$ — Auxiliary memory allocation bound.
