## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, linked list node pointer manipulation (`val`, `next`). Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(q)$ — Operation count bound.
- **Space Complexity**: $O(U + B)$ — Auxiliary memory allocation bound.
