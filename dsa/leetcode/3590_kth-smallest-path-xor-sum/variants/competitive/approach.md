## General
Algorithm uses depth-first search recursion. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n log^2 n + q log n)$ — Operation count bound.
- **Space Complexity**: $O(n log n + q)$ — Auxiliary memory allocation bound.
