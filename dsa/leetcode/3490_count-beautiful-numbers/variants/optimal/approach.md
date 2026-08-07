## General
Given two positive integers, `l` and `r`. A positive integer is called **beautiful** if the product of its digits is divisible by the sum of its digits, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(D^4)$ — Operation count bound.
- **Space Complexity**: $O(D^3)$ — Auxiliary memory allocation bound.
