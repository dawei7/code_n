## General
Maintains double-ended queue (`deque`) for $O(1)$ window bounds. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(Q)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
