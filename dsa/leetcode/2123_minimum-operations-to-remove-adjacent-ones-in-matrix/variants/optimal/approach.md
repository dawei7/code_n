## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(E sqrt V)$ — Operation count bound.
- **Space Complexity**: $O(V + E)$ — Auxiliary memory allocation bound.
