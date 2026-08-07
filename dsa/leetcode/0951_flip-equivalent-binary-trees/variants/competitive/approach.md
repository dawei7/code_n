## General
Algorithm uses two-pointer sliding window iteration. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, tree node traversal (`val`, `left`, `right`). Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(h)$ — Auxiliary memory allocation bound.
