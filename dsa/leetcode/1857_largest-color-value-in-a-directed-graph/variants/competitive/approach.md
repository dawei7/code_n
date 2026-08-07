## General
Given There is a **directed graph** of `n` colored nodes and `m` edges. The nodes are numbered from `0` to $n - 1$, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(26(n+m))$ — Operation count bound.
- **Space Complexity**: $O(26n+m)$ — Auxiliary memory allocation bound.
