## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n log n + n log k log side)$ — Operation count bound.
- **Space Complexity**: $O(n log k)$ — Auxiliary memory allocation bound.
