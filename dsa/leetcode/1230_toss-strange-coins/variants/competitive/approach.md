## General
Given You have some coins.  The `i`-th coin has a probability $\text{prob}[i]$ of facing heads when tossed, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(nt)$ — Operation count bound.
- **Space Complexity**: $O(t)$ — Auxiliary memory allocation bound.
