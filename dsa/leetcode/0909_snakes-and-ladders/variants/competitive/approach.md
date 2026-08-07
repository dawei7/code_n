## General
Given an `n x n` integer matrix `board` where the cells are labeled from `1` to $n^{2}$ in a <a href="https://en.wikipedia.org/wiki/Boustrophedon" target="_blank">**Boustrophedon style**</a> starting from the bottom left of..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n^2)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
