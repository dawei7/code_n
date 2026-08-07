## General
Algorithm uses single-pass sequential scanning. Maintains double-ended queue (`deque`) for $O(1)$ window bounds, priority queue (`heapq`) for dynamic ordering. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m n 3^n log(m 2^n))$ — Operation count bound.
- **Space Complexity**: $O(m n 3^n)$ — Auxiliary memory allocation bound.
