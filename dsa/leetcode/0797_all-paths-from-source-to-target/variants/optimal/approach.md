## General
Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to $n - 1$, find all possible paths from node `0` to node $n - 1$ and return them in **any order**, the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(V + E + P \cdot V)$ — Operation count bound.
- **Space Complexity**: $O(V + E + P \cdot V)$ — Auxiliary memory allocation bound.
