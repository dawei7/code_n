## General
Algorithm uses breadth-first search queue level traversal. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M log log M + n log M)$ — Operation count bound.
- **Space Complexity**: $O(M + n)$ — Auxiliary memory allocation bound.
