## General
Algorithm uses depth-first search recursion. Maintains double-ended queue (`deque`) for $O(1)$ window bounds. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(p B + p^2 2^p)$ — Operation count bound.
- **Space Complexity**: $O(B + p 2^p)$ — Auxiliary memory allocation bound.
