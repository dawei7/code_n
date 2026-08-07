## General
Given There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are `(x, y)`, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(B^2)$ — Operation count bound.
- **Space Complexity**: $O(B^2)$ — Auxiliary memory allocation bound.
