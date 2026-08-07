## General
Algorithm uses two-pointer sliding window iteration. Maintains priority queue (`heapq`) for dynamic ordering. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n\log n+m\log m)$ — Operation count bound.
- **Space Complexity**: $O(n+m)$ — Auxiliary memory allocation bound.
