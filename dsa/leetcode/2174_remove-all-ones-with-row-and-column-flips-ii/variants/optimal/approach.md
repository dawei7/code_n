## General
Given a **0-indexed** `m x n` **binary** matrix `grid`, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(k 2^k)$ — Operation count bound.
- **Space Complexity**: $O(2^k)$ — Auxiliary memory allocation bound.
