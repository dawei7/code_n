## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed, double-ended queue (`deque`) for $O(1)$ window bounds, dynamic programming memoization array/table. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(m * n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
