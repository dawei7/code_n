## General
Given an integer array `weights` and two integers `w1` and `w2` representing the **maximum** capacities of two bags, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(n * w1 * w2)$ — Operation count bound.
- **Space Complexity**: $O(w1 * w2)$ — Auxiliary memory allocation bound.
