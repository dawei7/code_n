## General
Algorithm uses single-pass sequential scanning. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, tree node traversal (`val`, `left`, `right`). Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n C_n)$ — Operation count bound.
- **Space Complexity**: $O(n C_n)$ — Auxiliary memory allocation bound.
