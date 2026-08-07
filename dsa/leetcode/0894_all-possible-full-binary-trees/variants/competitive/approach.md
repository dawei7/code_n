## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table, tree node traversal (`val`, `left`, `right`). Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nF(n))$ — Operation count bound.
- **Space Complexity**: $O(nF(n))$ — Auxiliary memory allocation bound.
