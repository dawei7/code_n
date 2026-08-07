## General
Algorithm uses depth-first search recursion. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(V + E)$ — Operation count bound.
- **Space Complexity**: $O(V + E)$ — Auxiliary memory allocation bound.
