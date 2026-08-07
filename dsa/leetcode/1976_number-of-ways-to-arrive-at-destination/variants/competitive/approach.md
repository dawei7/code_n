## General
Given You are in a city that consists of `n` intersections numbered from `0` to $n - 1$ with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any ot..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering, a dynamic programming memoization table to cache intermediate subproblem states. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O((V+E)\log V)$ — Operation count bound.
- **Space Complexity**: $O(V+E)$ — Auxiliary memory allocation bound.
