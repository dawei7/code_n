## General
Given an array of **distinct** positive integers locations where $\text{locations}[i]$ represents the position of city `i`. You are also given integers `start`, `finish` and `fuel` representing the starting city, ending cit..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(N^2F)$ — Operation count bound.
- **Space Complexity**: $O(NF)$ — Auxiliary memory allocation bound.
