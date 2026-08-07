## General
Given a 2D integer matrix `grid` of size `n x m`, where each element is either `0`, `1`, or `2`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(nm)$ — Operation count bound.
- **Space Complexity**: $O(nm)$ — Auxiliary memory allocation bound.
