## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(2^N(N^3 + R))$ — Operation count bound.
- **Space Complexity**: $O(N^2)$ — Auxiliary memory allocation bound.
