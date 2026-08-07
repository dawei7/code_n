## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n \log(R / \varepsilon))$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
