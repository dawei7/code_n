## General
Algorithm uses binary search over sorted domain. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(n log(P))$ — Operation count bound.
- **Space Complexity**: $O(n + P)$ — Auxiliary memory allocation bound.
