## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(N \log K)$ — Operation count bound.
- **Space Complexity**: $O(U)$ — Auxiliary memory allocation bound.
