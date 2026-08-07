## General
Given an integer array `cost` where $\text{cost}[i]$ is the cost of $$i^{\text{th}}$$ step on a staircase. Once you pay the cost, you can either climb one or two steps, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
