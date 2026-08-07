## General
Given an integer `n`, the number of nodes in a directed graph where the nodes are labeled from `0` to $n - 1$. Each edge is red or blue in this graph, and there could be self-edges and parallel edges, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n + r + b)$ — Operation count bound.
- **Space Complexity**: $O(n + r + b)$ — Auxiliary memory allocation bound.
