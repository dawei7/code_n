## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards.

## Complexity detail
- **Time Complexity**: $O(sum(|word|^2))$ — Operation count bound.
- **Space Complexity**: $O(sum(|word|))$ — Auxiliary memory allocation bound.
