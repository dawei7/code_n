## General
Algorithm uses two-pointer sliding window iteration. Maintains hash set (`set`) for $O(1)$ duplicate check, priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(MN\min(M,N))$ — Operation count bound.
- **Space Complexity**: $O(MN)$ — Auxiliary memory allocation bound.
