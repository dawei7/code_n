## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n_1+n_2)$ — Operation count bound.
- **Space Complexity**: $O(h+u)$ — Auxiliary memory allocation bound.
