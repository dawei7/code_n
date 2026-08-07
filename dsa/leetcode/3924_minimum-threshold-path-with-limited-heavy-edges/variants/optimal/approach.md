## General
Algorithm uses binary search over sorted domain. Maintains double-ended queue (`deque`) for $O(1)$ window bounds. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n log m + m log m)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
