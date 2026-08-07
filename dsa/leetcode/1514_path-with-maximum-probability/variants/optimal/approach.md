## General
Algorithm uses single-pass sequential scanning. Maintains priority queue (`heapq`) for dynamic ordering. Applies walrus operator (`:=`) for inline assignment and zero-copy conditional check.

## Complexity detail
- **Time Complexity**: $O((n+e)\log n)$ — Operation count bound.
- **Space Complexity**: $O(n+e)$ — Auxiliary memory allocation bound.
