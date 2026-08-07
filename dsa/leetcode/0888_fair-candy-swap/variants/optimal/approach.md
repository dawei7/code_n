## General
Algorithm uses single-pass sequential scanning. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates, walrus operator (`:=`) for inline assignment and zero-copy conditional check.

## Complexity detail
- **Time Complexity**: $O(p+q)$ — Operation count bound.
- **Space Complexity**: $O(q)$ — Auxiliary memory allocation bound.
