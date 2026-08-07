## General
Given There are `n` people and `40` types of hats labeled from `1` to `40`, the algorithm executes a single-pass linear scan through input elements. It utilizes a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(40p2^p)$ — Operation count bound.
- **Space Complexity**: $O(2^p)$ — Auxiliary memory allocation bound.
