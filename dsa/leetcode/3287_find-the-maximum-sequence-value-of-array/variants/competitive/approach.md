## General
Given an integer array `nums` and a **positive** integer `k`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n(kB + B^2))$ — Operation count bound.
- **Space Complexity**: $O((n + k)B)$ — Auxiliary memory allocation bound.
