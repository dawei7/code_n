## General
Algorithm uses depth-first search recursion. Maintains hash set (`set`) for $O(1)$ duplicate check. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O((mn)^2)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
