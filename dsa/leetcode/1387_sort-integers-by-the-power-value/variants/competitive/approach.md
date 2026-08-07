## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, dynamic programming memoization array/table. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(U + R log R)$ — Operation count bound.
- **Space Complexity**: $O(U + R)$ — Auxiliary memory allocation bound.
