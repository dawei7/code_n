## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed, double-ended queue (`deque`) for $O(1)$ window bounds.

## Complexity detail
- **Time Complexity**: $O(n log m + m log m)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
