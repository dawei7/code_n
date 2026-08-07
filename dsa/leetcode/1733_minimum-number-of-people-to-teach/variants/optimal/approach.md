## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(S + C)$ — Operation count bound.
- **Space Complexity**: $O(S + m)$ — Auxiliary memory allocation bound.
