## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(q^2 log q)$ — Operation count bound.
- **Space Complexity**: $O(q + S)$ — Auxiliary memory allocation bound.
