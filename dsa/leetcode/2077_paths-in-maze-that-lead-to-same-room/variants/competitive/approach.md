## General
Algorithm uses single-pass sequential scanning. Maintains hash set (`set`) for $O(1)$ duplicate check. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n+E^{3/2})$ — Operation count bound.
- **Space Complexity**: $O(n+E)$ — Auxiliary memory allocation bound.
