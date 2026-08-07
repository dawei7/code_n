## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(RC)$ — Operation count bound.
- **Space Complexity**: $O(\max(R,C))$ — Auxiliary memory allocation bound.
