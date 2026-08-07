## General
Algorithm uses depth-first search recursion. Maintains hash set (`set`) for $O(1)$ duplicate check. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n+e+4^L)$ — Operation count bound.
- **Space Complexity**: $O(n+e+L)$ — Auxiliary memory allocation bound.
