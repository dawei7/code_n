## General
Algorithm uses two-pointer sliding window iteration. Maintains dynamic programming memoization array/table, tree node traversal (`val`, `left`, `right`). Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
