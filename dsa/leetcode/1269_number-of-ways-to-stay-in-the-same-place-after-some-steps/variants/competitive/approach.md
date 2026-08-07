## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(\texttt{steps}\,w)$ — Operation count bound.
- **Space Complexity**: $O(w)$ — Auxiliary memory allocation bound.
