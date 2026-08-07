## General
Algorithm uses breadth-first search queue level traversal. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, dynamic programming memoization array/table.

## Complexity detail
- **Time Complexity**: $O(R\log R+F\log F+RF)$ — Operation count bound.
- **Space Complexity**: $O(R+F)$ — Auxiliary memory allocation bound.
