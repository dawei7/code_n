## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check, priority queue (`heapq`) for dynamic ordering. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(U log log U + (n + q) log(n + q))$ — Operation count bound.
- **Space Complexity**: $O(U + n + q)$ — Auxiliary memory allocation bound.
