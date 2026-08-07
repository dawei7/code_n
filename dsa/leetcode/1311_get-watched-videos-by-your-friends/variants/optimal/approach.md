## General
Algorithm uses breadth-first search queue level traversal. Maintains hash map lookup (`dict`) for $O(1)$ average speed, double-ended queue (`deque`) for $O(1)$ window bounds.

## Complexity detail
- **Time Complexity**: $O(n+E+S+Vlog V)$ — Operation count bound.
- **Space Complexity**: $O(n+V)$ — Auxiliary memory allocation bound.
