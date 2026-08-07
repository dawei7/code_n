## General
Given an `m x n` grid `grid` where:, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(mn2^c)$ — Operation count bound.
- **Space Complexity**: $O(mn2^c)$ — Auxiliary memory allocation bound.
