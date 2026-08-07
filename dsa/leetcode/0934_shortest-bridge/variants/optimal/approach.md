## General
Given an `n x n` binary matrix `grid` where `1` represents land and `0` represents water, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
