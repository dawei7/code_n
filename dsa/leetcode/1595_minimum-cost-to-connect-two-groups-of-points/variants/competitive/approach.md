## General
Given two groups of points where the first group has $\text{size}_{1}$ points, the second group has $\text{size}_{2}$ points, and $\text{size}_{1} \ge \text{size}_{2}$, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(mn2^n)$ — Operation count bound.
- **Space Complexity**: $O(m2^n)$ — Auxiliary memory allocation bound.
