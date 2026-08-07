## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering.

## Complexity detail
- **Time Complexity**: $O(k + \log U + p \log p)$ — Operation count bound.
- **Space Complexity**: $O(U + H)$ — Auxiliary memory allocation bound.
