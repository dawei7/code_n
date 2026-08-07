## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O((n + m) log n)$ — Operation count bound.
- **Space Complexity**: $O(n log n)$ — Auxiliary memory allocation bound.
