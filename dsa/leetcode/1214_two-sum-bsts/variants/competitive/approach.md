## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, tree node traversal (`val`, `left`, `right`). Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n+m)$ — Operation count bound.
- **Space Complexity**: $O(n+m)$ — Auxiliary memory allocation bound.
