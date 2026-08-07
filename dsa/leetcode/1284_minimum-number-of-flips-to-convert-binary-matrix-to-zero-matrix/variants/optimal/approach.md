## General
Algorithm uses breadth-first search queue level traversal. Maintains double-ended queue (`deque`) for $O(1)$ window bounds. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(k2^k)$ — Operation count bound.
- **Space Complexity**: $O(2^k)$ — Auxiliary memory allocation bound.
