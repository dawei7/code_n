## General
Algorithm uses two-pointer sliding window iteration. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n log V)$ — Operation count bound.
- **Space Complexity**: $O(log V)$ — Auxiliary memory allocation bound.
