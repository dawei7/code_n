## General
Given Design a queue that supports `push` and `pop` operations in the front, middle, and back, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(q)$ — Operation count bound.
- **Space Complexity**: $O(q)$ — Auxiliary memory allocation bound.
