## General
Algorithm uses single-pass sequential scanning. Maintains hash set (`set`) for $O(1)$ duplicate check. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(2^k)$ — Auxiliary memory allocation bound.
