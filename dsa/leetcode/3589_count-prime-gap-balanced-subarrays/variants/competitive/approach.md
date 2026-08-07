## General
Algorithm uses breadth-first search queue level traversal. Maintains double-ended queue (`deque`) for $O(1)$ window bounds. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(V log log V + n)$ — Operation count bound.
- **Space Complexity**: $O(V + n)$ — Auxiliary memory allocation bound.
