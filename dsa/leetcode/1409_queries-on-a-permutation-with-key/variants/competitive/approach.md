## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((m+q)\log(m+q))$ — Operation count bound.
- **Space Complexity**: $O(m+q)$ — Auxiliary memory allocation bound.
