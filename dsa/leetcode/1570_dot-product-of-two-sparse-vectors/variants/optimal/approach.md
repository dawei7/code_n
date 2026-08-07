## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(N + \min(K_1,K_2))$ — Operation count bound.
- **Space Complexity**: $O(K_1+K_2)$ — Auxiliary memory allocation bound.
