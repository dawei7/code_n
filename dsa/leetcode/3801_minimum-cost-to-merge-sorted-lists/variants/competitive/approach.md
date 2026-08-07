## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(3^L + N * 2^L + N log N)$ — Operation count bound.
- **Space Complexity**: $O(2^L + N)$ — Auxiliary memory allocation bound.
