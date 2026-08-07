## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed, hash set (`set`) for $O(1)$ duplicate check, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n_1n_2B)$ — Operation count bound.
- **Space Complexity**: $O(n_1n_2B)$ — Auxiliary memory allocation bound.
