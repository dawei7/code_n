## General
Algorithm uses breadth-first search queue level traversal. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, tree node traversal (`val`, `left`, `right`). Edge cases: handles empty/null inputs via early return guards, uses infinity sentinels for extreme boundary comparisons.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
