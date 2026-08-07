## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, tree node traversal (`val`, `left`, `right`). Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(nD^2)$ — Operation count bound.
- **Space Complexity**: $O(hD)$ — Auxiliary memory allocation bound.
