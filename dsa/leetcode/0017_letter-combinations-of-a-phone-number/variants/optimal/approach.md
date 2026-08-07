## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n \cdot 4^n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
