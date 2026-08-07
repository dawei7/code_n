## General
Algorithm uses breadth-first search queue level traversal. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check, double-ended queue (`deque`) for $O(1)$ window bounds. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(T+PM)$ — Operation count bound.
- **Space Complexity**: $O(L)$ — Auxiliary memory allocation bound.
