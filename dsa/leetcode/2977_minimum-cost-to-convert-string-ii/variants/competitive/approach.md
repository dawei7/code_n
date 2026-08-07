## General
Uses single-pass sequential iteration. Maintains hash map (`dict`) for $O(1)$ average lookup, priority queue (`heapq`) for dynamic minimum/maximum tracking, dynamic programming memoization store. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`).

## Complexity detail
- **Time Complexity**: $O(M^3 + N^2 + S)$ — Operation count bound.
- **Space Complexity**: $O(M^2 + N + S)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Algorithm design:** Describes the specific algorithmic approach used in the solution.
- **Complexity bounds:** Declares the precise time and space complexity guarantees.
