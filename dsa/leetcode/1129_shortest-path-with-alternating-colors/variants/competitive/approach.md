## General
Algorithm uses breadth-first search queue level traversal. Maintains hash set (`set`) for $O(1)$ duplicate check, double-ended queue (`deque`) for $O(1)$ window bounds. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n + r + b)$ — Operation count bound.
- **Space Complexity**: $O(n + r + b)$ — Auxiliary memory allocation bound.
