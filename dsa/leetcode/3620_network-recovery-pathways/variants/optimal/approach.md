## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O((n + m) log m)$ — Operation count bound.
- **Space Complexity**: $O(n + m)$ — Auxiliary memory allocation bound.
