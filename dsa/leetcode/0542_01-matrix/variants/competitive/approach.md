## General
Given an `m x n` binary matrix `mat`, return *the distance of the nearest *`0`* for each cell*, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, a dynamic programming memoization table to cache intermediate subproblem states. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(rows \cdot cols)$ — Operation count bound.
- **Space Complexity**: $O(rows \cdot cols)$ — Auxiliary memory allocation bound.
