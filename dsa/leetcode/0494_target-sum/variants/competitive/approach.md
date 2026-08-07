## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, dynamic programming memoization array/table. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n \cdot total)$ — Operation count bound.
- **Space Complexity**: $O(total)$ — Auxiliary memory allocation bound.
