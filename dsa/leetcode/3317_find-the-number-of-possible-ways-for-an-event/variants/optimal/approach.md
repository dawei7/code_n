## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n min(n, x))$ — Operation count bound.
- **Space Complexity**: $O(min(n, x))$ — Auxiliary memory allocation bound.
