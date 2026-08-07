## General
Algorithm uses depth-first search recursion. Maintains hash set (`set`) for $O(1)$ duplicate check. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(k^n)$ — Operation count bound.
- **Space Complexity**: $O(k^n)$ — Auxiliary memory allocation bound.
