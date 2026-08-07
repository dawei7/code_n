## General
Algorithm uses single-pass sequential scanning. Maintains priority queue (`heapq`) for dynamic ordering. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nk)$ — Operation count bound.
- **Space Complexity**: $O(n + k)$ — Auxiliary memory allocation bound.
