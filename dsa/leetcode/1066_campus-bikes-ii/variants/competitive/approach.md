## General
Algorithm uses single-pass sequential scanning. Maintains hash set (`set`) for $O(1)$ duplicate check, priority queue (`heapq`) for dynamic ordering, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(B2^B)$ — Operation count bound.
- **Space Complexity**: $O(2^B)$ — Auxiliary memory allocation bound.
