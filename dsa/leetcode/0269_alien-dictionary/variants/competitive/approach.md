## General
Algorithm uses depth-first search recursion. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check, double-ended queue (`deque`) for $O(1)$ window bounds. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(c + e)$ — Operation count bound.
- **Space Complexity**: $O(a + e)$ — Auxiliary memory allocation bound.
