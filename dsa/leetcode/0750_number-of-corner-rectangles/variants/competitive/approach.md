## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(mn \min(m,n))$ — Operation count bound.
- **Space Complexity**: $O(\min(m,n)^2)$ — Auxiliary memory allocation bound.
