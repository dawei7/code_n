## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(nL + q)$ — Operation count bound.
- **Space Complexity**: $O(n + q)$ — Auxiliary memory allocation bound.
