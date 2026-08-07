## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((N + Q) log (N + Q) + Q log V)$ — Operation count bound.
- **Space Complexity**: $O(N + Q)$ — Auxiliary memory allocation bound.
