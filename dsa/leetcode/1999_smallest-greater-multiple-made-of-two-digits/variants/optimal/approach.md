## General
Given three integers, `k`, `digit1`, and `digit2`, you want to find the **smallest** integer that is:, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(2^D)$ — Operation count bound.
- **Space Complexity**: $O(2^D)$ — Auxiliary memory allocation bound.
