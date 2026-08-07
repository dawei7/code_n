## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering.

## Complexity detail
- **Time Complexity**: $O(1) / O(F + 10 \log F)$ — Operation count bound.
- **Space Complexity**: $O(U + E)$ — Auxiliary memory allocation bound.
