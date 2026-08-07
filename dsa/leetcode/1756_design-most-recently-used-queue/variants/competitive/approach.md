## General
Given Design a queue-like data structure that moves the most recently used element to the end of the queue, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(\sqrt{n})$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
