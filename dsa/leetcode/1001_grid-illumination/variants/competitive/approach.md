## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(L+Q)$ — Operation count bound.
- **Space Complexity**: $O(L)$ — Auxiliary memory allocation bound.
