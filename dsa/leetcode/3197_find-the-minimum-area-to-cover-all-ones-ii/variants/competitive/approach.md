## General
Algorithm uses binary search over sorted domain. Maintains hash map lookup (`dict`) for $O(1)$ average speed, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((R + C)(R^2 + RC + C^2))$ — Operation count bound.
- **Space Complexity**: $O(RC + R^2 + C^2)$ — Auxiliary memory allocation bound.
