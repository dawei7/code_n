## General
Algorithm uses single-pass sequential scanning. Maintains hash set (`set`) for $O(1)$ duplicate check. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + m)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
