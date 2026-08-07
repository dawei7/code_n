## General
Given You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an `m x n` matrix. In this matrix:, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends, a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(T \log T + TRC)$ — Operation count bound.
- **Space Complexity**: $O(RC)$ — Auxiliary memory allocation bound.
