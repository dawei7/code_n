## General
Algorithm uses two-pointer sliding window iteration. Maintains double-ended queue (`deque`) for $O(1)$ window bounds. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O((n + m)m)$ — Operation count bound.
- **Space Complexity**: $O((n + m)m)$ — Auxiliary memory allocation bound.
