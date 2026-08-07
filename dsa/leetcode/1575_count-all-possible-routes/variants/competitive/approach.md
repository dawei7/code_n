## General
Given an array of **distinct** positive integers locations where $\text{locations}[i]$ represents the position of city `i`. You are also given integers `start`, `finish` and `fuel` representing the starting city, ending cit..., the algorithm executes binary search over the search space to achieve logarithmic reduction. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N^2F)$ — Operation count bound.
- **Space Complexity**: $O(NF)$ — Auxiliary memory allocation bound.
