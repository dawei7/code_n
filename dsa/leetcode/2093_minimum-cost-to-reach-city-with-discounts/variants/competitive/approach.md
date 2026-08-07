## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, priority queue (`heapq`) for dynamic ordering. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(E(K+1)\log(n(K+1)))$ — Operation count bound.
- **Space Complexity**: $O((n+E)(K+1))$ — Auxiliary memory allocation bound.
