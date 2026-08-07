## General
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(m)$ — Operation count bound.
- **Space Complexity**: $O(size)$ — Auxiliary memory allocation bound.
