## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2 * 2^n)$ — Operation count bound.
- **Space Complexity**: $O(2^n)$ — Auxiliary memory allocation bound.
