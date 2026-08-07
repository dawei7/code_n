## General
Given a **0-indexed** 2D integer matrix `grid` of size $3 * 3$, representing the number of stones in each cell. The grid contains exactly `9` stones, and there can be **multiple** stones in a single cell, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(k \cdot 2^k)$ — Operation count bound.
- **Space Complexity**: $O(2^k)$ — Auxiliary memory allocation bound.
