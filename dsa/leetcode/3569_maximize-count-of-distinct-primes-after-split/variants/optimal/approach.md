## General
Uses binary search over search space. Maintains hash map (`dict`) for $O(1)$ average lookup, hash set (`set`) for $O(1)$ existence checks, priority queue (`heapq`) for dynamic minimum/maximum tracking.

## Complexity detail
- **Time Complexity**: $O(U log log U + (n + q) log(n + q))$ — Operation count bound.
- **Space Complexity**: $O(U + n + q)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Algorithm design:** Describes the specific algorithmic approach used in the solution.
- **Complexity bounds:** Declares the precise time and space complexity guarantees.
