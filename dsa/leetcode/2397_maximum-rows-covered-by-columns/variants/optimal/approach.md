## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(mn + (m + k) C(n,k))$ — Operation count bound.
- **Space Complexity**: $O(m)$ — Auxiliary memory allocation bound.
