## General
Algorithm uses breadth-first search queue level traversal. Maintains hash map lookup (`dict`) for $O(1)$ average speed, dynamic programming memoization array/table. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(m * 2^m + n)$ — Operation count bound.
- **Space Complexity**: $O(2^m)$ — Auxiliary memory allocation bound.
