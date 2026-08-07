## General
Given two integers `n` and `x`. You have to construct an array of **positive** integers `nums` of size `n` where for every $0 \le i < n - 1$, $nums[i + 1]$ is **greater than** $\text{nums}[i]$, and the result of the bitwise..., the algorithm solves **Minimum Array End** directly. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(log n + log x)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
