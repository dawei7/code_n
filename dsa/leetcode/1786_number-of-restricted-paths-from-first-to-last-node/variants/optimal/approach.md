## General
Algorithm uses depth-first search recursion. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((n+E)\log n)$ — Operation count bound.
- **Space Complexity**: $O(n+E)$ — Auxiliary memory allocation bound.
