## General
Given A game on an **undirected** graph is played by two players, Mouse and Cat, who alternate turns, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^3)$ — Operation count bound.
- **Space Complexity**: $O(n^2)$ — Auxiliary memory allocation bound.
