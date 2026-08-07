## General
Given an array of `words` where each word consists of lowercase English letters, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(W log W+WL^2)$ — Operation count bound.
- **Space Complexity**: $O(WL)$ — Auxiliary memory allocation bound.
