## General
Given There are `n` types of units indexed from `0` to $n - 1$, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n + Q)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
