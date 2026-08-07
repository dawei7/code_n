## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering.

## Complexity detail
- **Time Complexity**: $O(P(n + m) log(nP))$ — Operation count bound.
- **Space Complexity**: $O(nP + m)$ — Auxiliary memory allocation bound.
