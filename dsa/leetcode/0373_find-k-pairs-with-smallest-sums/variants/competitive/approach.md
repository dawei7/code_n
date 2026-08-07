## General
Algorithm uses single-pass sequential scanning. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(k \log \min(k,m))$ — Operation count bound.
- **Space Complexity**: $O(\min(k,m))$ — Auxiliary memory allocation bound.
