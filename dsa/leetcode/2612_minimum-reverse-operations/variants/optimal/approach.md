## General
Algorithm uses breadth-first search queue level traversal. Maintains double-ended queue (`deque`) for $O(1)$ window bounds. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n\alpha(n))$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
