## General
Algorithm uses single-pass sequential scanning. Maintains priority queue (`heapq`) for dynamic ordering, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(mn log(mn))$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
