## General
Algorithm uses depth-first search recursion. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O\left(wh(h+1)^w\right)$ — Operation count bound.
- **Space Complexity**: $O\left((h+1)^w\right)$ — Auxiliary memory allocation bound.
