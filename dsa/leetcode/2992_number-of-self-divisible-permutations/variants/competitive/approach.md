## General
Given an integer `n`, return *the number of **permutations** of the **1-indexed** array* `nums = [1, 2, ..., n]`*, such that it's **self-divisible***, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N 2^N)$ — Operation count bound.
- **Space Complexity**: $O(2^N)$ — Auxiliary memory allocation bound.
