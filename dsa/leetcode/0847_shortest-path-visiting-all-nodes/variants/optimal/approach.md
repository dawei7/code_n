## General
Given You have an undirected, connected graph of `n` nodes labeled from `0` to $n - 1$. You are given an array `graph` where $\text{graph}[i]$ is a list of all the nodes connected with node `i` by an edge, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(n^2 \cdot 2^n)$ — Operation count bound.
- **Space Complexity**: $O(n \cdot 2^n)$ — Auxiliary memory allocation bound.
