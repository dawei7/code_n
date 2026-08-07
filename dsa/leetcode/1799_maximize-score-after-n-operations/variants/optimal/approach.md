## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates, walrus operator (`:=`) for inline assignment and zero-copy conditional check. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(m^2 2^m)$ — Operation count bound.
- **Space Complexity**: $O(m^2 + 2^m)$ — Auxiliary memory allocation bound.
