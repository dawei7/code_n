## General
Given There is a directed graph of `n` nodes with each node labeled from `0` to $n - 1$. The graph is represented by a **0-indexed** 2D integer array `graph` where $\text{graph}[i]$ is an integer array of nodes adjacent to ..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(V + E)$ — Operation count bound.
- **Space Complexity**: $O(V + E)$ — Auxiliary memory allocation bound.
