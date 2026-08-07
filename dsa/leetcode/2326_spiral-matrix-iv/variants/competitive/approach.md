## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, linked list node pointer manipulation (`val`, `next`). Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
