## General
Given an `m x n` grid `rooms` initialized with these three possible values, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(mn)$ — Operation count bound.
- **Space Complexity**: $O(mn)$ — Auxiliary memory allocation bound.
