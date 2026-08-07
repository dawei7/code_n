## General
Given two strings, `source` and `target`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a dynamic programming memoization table to cache intermediate subproblem states.

## Complexity detail
- **Time Complexity**: $O(nRL)$ — Operation count bound.
- **Space Complexity**: $O(n+R)$ — Auxiliary memory allocation bound.
