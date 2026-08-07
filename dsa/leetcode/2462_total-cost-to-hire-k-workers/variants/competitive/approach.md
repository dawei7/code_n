## General
Algorithm uses two-pointer sliding window iteration. Maintains priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O((c + k) log c)$ — Operation count bound.
- **Space Complexity**: $O(c)$ — Auxiliary memory allocation bound.
