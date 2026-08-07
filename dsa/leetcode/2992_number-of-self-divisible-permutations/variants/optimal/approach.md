## General
Given an integer `n`, return *the number of **permutations** of the **1-indexed** array* `nums = [1, 2, ..., n]`*, such that it's **self-divisible***, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(N 2^N)$ — Operation count bound.
- **Space Complexity**: $O(2^N)$ — Auxiliary memory allocation bound.
