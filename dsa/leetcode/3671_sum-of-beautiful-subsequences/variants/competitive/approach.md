## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(V log log V + n sqrt(V) + T log V)$ — Operation count bound.
- **Space Complexity**: $O(V log V)$ — Auxiliary memory allocation bound.
