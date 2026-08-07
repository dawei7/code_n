## General
Algorithm uses two-pointer sliding window iteration. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, priority queue (`heapq`) for dynamic ordering.

## Complexity detail
- **Time Complexity**: $O(n log n (n + m))$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
