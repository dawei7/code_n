## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, tree node traversal (`val`, `left`, `right`). Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(N+D)$ — Operation count bound.
- **Space Complexity**: $O(N+D)$ — Auxiliary memory allocation bound.
