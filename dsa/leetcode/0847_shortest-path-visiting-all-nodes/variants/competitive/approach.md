## General
Algorithm uses breadth-first search queue level traversal. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2 \cdot 2^n)$ — Operation count bound.
- **Space Complexity**: $O(n \cdot 2^n)$ — Auxiliary memory allocation bound.
