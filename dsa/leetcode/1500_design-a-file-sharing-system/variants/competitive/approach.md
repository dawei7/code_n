## General
Uses single-pass sequential iteration. Maintains hash map (`dict`) for $O(1)$ average lookup, hash set (`set`) for $O(1)$ existence checks, priority queue (`heapq`) for dynamic minimum/maximum tracking. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`).

## Complexity detail
- **Time Complexity**: $O(k + \log U + p \log p)$ — Operation count bound.
- **Space Complexity**: $O(U + H)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Algorithm design:** Describes the specific algorithmic approach used in the solution.
- **Complexity bounds:** Declares the precise time and space complexity guarantees.
