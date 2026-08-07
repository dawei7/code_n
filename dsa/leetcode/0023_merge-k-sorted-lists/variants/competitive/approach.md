## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering, linked list node pointer manipulation (`val`, `next`). Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(N \log k)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
