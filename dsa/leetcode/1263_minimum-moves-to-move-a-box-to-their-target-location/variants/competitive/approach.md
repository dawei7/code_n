## General
Algorithm uses single-pass sequential scanning. Maintains hash set (`set`) for $O(1)$ duplicate check. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(V^2)$ — Operation count bound.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.
