## General
Algorithm uses two-pointer sliding window iteration. Maintains hash set (`set`) for $O(1)$ duplicate check. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(m\log n+m\log m)$ — Operation count bound.
- **Space Complexity**: $O(m)$ — Auxiliary memory allocation bound.
