## General
Algorithm uses single-pass sequential scanning. Maintains dynamic programming memoization array/table. Edge cases: handles empty/null inputs via early return guards, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(MN)$ — Operation count bound.
- **Space Complexity**: $O(\min(M,N))$ — Auxiliary memory allocation bound.
