## General
Algorithm uses two-pointer sliding window iteration. Applies walrus operator (`:=`) for inline assignment and zero-copy conditional check. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(R log log R)$ — Operation count bound.
- **Space Complexity**: $O(R)$ — Auxiliary memory allocation bound.
