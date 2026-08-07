## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n\log(\ell+1))$ — Operation count bound.
- **Space Complexity**: $O(\ell)$ — Auxiliary memory allocation bound.
