## General
Algorithm uses depth-first search recursion. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n \cdot 2^n)$ — Operation count bound.
- **Space Complexity**: $O(2^n)$ — Auxiliary memory allocation bound.
