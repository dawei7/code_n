## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(RC)$ — Operation count bound.
- **Space Complexity**: $O(RC)$ — Auxiliary memory allocation bound.
