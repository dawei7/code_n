## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((n + q)\log(n + q) + (n + q)B)$ — Operation count bound.
- **Space Complexity**: $O(nB + q)$ — Auxiliary memory allocation bound.
