## General
Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or *`false`* otherwise*, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nT)$ — Operation count bound.
- **Space Complexity**: $O(T)$ — Auxiliary memory allocation bound.
