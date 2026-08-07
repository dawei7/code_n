## General
Algorithm uses breadth-first search queue level traversal. Maintains hash map lookup (`dict`) for $O(1)$ average speed, double-ended queue (`deque`) for $O(1)$ window bounds. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(U + q\log U)$ — Operation count bound.
- **Space Complexity**: $O(m+U)$ — Auxiliary memory allocation bound.
