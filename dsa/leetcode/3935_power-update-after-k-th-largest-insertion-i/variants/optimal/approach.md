## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((N + Q) log(N + Q) + Q log V)$ — Operation count bound.
- **Space Complexity**: $O(N + Q)$ — Auxiliary memory allocation bound.
