## General
Algorithm uses breadth-first search queue level traversal. Maintains hash set (`set`) for $O(1)$ duplicate check, double-ended queue (`deque`) for $O(1)$ window bounds, priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(T \log T + TRC)$ — Operation count bound.
- **Space Complexity**: $O(RC)$ — Auxiliary memory allocation bound.
