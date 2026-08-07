## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + A^3 log t)$ — Operation count bound.
- **Space Complexity**: $O(A^2)$ — Auxiliary memory allocation bound.
