## General
Given positive integers `low`, `high`, and `k`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(D^2 k)$ — Operation count bound.
- **Space Complexity**: $O(D^2 k)$ — Auxiliary memory allocation bound.
