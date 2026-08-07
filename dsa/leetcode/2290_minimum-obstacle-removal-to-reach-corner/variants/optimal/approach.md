## General
Given a **0-indexed** 2D integer array `grid` of size `m x n`. Each cell has one of two values:, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
