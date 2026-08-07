## General
Algorithm uses breadth-first search queue level traversal. Maintains double-ended queue (`deque`) for $O(1)$ window bounds. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((n + m) log n)$ — Operation count bound.
- **Space Complexity**: $O(n log n)$ — Auxiliary memory allocation bound.
