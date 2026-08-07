## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(M^3 + N^2 + S)$ — Operation count bound.
- **Space Complexity**: $O(M^2 + N + S)$ — Auxiliary memory allocation bound.
