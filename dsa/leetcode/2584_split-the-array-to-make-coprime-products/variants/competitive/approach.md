## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M log log M + n log M)$ — Operation count bound.
- **Space Complexity**: $O(M + n)$ — Auxiliary memory allocation bound.
