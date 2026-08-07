## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering. Applies walrus operator (`:=`) for inline assignment and zero-copy conditional check.

## Complexity detail
- **Time Complexity**: $O((n+m)\log n)$ — Operation count bound.
- **Space Complexity**: $O(n+m)$ — Auxiliary memory allocation bound.
