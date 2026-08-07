## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(d^2)$ — Operation count bound.
- **Space Complexity**: $O(d^2)$ — Auxiliary memory allocation bound.
