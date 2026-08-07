## General
Given an integer `n`, return the **maximum** integer `x` such that $x \le n$, and the bitwise `AND` of all the numbers in the range `[x, n]` is 0, the algorithm solves **Maximum Number That Makes Result of Bitwise AND Zero** directly. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(log n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
