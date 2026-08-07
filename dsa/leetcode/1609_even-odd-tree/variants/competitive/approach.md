## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, tree node traversal (`val`, `left`, `right`). Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(w)$ — Auxiliary memory allocation bound.
