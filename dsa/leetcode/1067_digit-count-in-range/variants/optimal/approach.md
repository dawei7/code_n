## General
Given a single-digit integer `d` and two integers `low` and `high`, return *the number of times that *`d`* occurs as a digit in all integers in the inclusive range *`[low, high]`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(\log H)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
