## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m n l sqrt(V))$ — Operation count bound.
- **Space Complexity**: $O(m n l)$ — Auxiliary memory allocation bound.
