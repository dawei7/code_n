## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check, double-ended queue (`deque`) for $O(1)$ window bounds, dynamic programming memoization array/table. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(S + T^2)$ — Operation count bound.
- **Space Complexity**: $O(S + T)$ — Auxiliary memory allocation bound.
