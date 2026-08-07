## General
Given a **0-indexed** 2D integer matrix `grid` of size $n * n$ with values in the range $[1, n^{2}]$. Each integer appears **exactly once** except `a` which appears **twice** and `b` which is **missing**. The task is to fin..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(N^2)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
