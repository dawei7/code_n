## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(V \log \log V + n \log n)$ — Operation count bound.
- **Space Complexity**: $O(V + n)$ — Auxiliary memory allocation bound.
