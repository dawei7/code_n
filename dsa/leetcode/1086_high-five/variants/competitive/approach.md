## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(N+S\log S)$ — Operation count bound.
- **Space Complexity**: $O(S)$ — Auxiliary memory allocation bound.
