## General
Algorithm uses single-pass sequential scanning. Maintains priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(k(n+m) log(nk))$ — Operation count bound.
- **Space Complexity**: $O(k(n+m))$ — Auxiliary memory allocation bound.
