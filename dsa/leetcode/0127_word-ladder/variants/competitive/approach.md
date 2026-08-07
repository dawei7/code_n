## General
Algorithm uses two-pointer sliding window iteration. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
