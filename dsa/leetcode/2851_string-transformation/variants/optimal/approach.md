## General
Given two strings `s` and `t` of equal length `n`. You can perform the following operation on the string `s`:, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + log k)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
