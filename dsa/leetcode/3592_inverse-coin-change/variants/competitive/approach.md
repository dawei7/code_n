## General
Given a **1-indexed** integer array `numWays`, where $\text{numWays}[i]$ represents the number of ways to select a total amount `i` using an **infinite** supply of some *fixed* coin denominations. Each denomination is a **p..., the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
