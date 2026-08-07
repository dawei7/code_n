## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(N + K + A^3)$ — Operation count bound.
- **Space Complexity**: $O(A^2)$ — Auxiliary memory allocation bound.
