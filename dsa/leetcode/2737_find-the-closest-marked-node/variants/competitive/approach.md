## General
Algorithm uses single-pass sequential scanning. Maintains priority queue (`heapq`) for dynamic ordering. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((n + e) log n)$ — Operation count bound.
- **Space Complexity**: $O(n + e)$ — Auxiliary memory allocation bound.
