## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(mn + m V log V)$ — Operation count bound.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.
