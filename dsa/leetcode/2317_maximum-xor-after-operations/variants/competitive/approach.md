## General
Given a **0-indexed** integer array `nums`. In one operation, select **any** non-negative integer `x` and an index `i`, then **update** $\text{nums}[i]$ to be equal to $\text{nums}[i] AND (\text{nums}[i] XOR x)$, the algorithm solves **Maximum XOR After Operations ** directly. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
