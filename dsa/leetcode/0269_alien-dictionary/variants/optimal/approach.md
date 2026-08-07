## General
Given There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(c + e)$ — Operation count bound.
- **Space Complexity**: $O(a + e)$ — Auxiliary memory allocation bound.
