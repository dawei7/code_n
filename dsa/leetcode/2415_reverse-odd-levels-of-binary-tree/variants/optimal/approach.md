## General
Algorithm uses two-pointer sliding window iteration. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, tree node traversal (`val`, `left`, `right`). Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(log n)$ — Auxiliary memory allocation bound.
