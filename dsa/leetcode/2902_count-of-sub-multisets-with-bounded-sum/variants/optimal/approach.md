## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, dynamic programming memoization array/table. Applies walrus operator (`:=`) for inline assignment and zero-copy conditional check. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + Dr)$ — Operation count bound.
- **Space Complexity**: $O(r)$ — Auxiliary memory allocation bound.
