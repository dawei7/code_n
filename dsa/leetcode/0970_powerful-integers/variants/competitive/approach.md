## General
Algorithm uses single-pass sequential scanning. Maintains hash set (`set`) for $O(1)$ duplicate check. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(AB)$ — Operation count bound.
- **Space Complexity**: $O(A+B+R)$ — Auxiliary memory allocation bound.
