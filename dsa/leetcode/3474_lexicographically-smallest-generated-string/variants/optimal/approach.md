## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O((n + m)m)$ — Operation count bound.
- **Space Complexity**: $O((n + m)m)$ — Auxiliary memory allocation bound.
