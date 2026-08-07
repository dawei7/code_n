## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check, dynamic programming memoization array/table. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n + U^2)$ — Operation count bound.
- **Space Complexity**: $O(U)$ — Auxiliary memory allocation bound.
