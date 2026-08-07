## General
Given an `n x n` binary matrix `grid` where `1` represents land and `0` represents water, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
