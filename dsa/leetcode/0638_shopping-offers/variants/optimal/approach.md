## General
Algorithm uses depth-first search recursion. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(SM \cdot \prod(needs_i + 1))$ — Operation count bound.
- **Space Complexity**: $O(M \cdot \prod(needs_i + 1))$ — Auxiliary memory allocation bound.
