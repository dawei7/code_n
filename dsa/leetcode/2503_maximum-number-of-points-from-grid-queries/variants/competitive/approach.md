## General
Algorithm uses breadth-first search queue level traversal. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(m n log(m n) + k log k)$ — Operation count bound.
- **Space Complexity**: $O(m n + k)$ — Auxiliary memory allocation bound.
