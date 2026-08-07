## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nC)$ — Operation count bound.
- **Space Complexity**: $O(n + C)$ — Auxiliary memory allocation bound.
