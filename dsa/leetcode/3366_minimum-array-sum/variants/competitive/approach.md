## General
Given an integer array `nums` and three integers `k`, `op1`, and `op2`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n * op1 * op2)$ — Operation count bound.
- **Space Complexity**: $O(op1 * op2)$ — Auxiliary memory allocation bound.
