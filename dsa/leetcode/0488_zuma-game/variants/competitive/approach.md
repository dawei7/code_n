## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O((n + h)^{h + 1})$ — Operation count bound.
- **Space Complexity**: $O((n + h)^h)$ — Auxiliary memory allocation bound.
