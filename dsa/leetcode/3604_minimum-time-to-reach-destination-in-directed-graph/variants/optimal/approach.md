## General
Algorithm uses single-pass sequential scanning. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, priority queue (`heapq`) for dynamic ordering.

## Complexity detail
- **Time Complexity**: $O((n + m) log n)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
