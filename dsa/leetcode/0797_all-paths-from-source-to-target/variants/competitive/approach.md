## General
Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to $n - 1$, find all possible paths from node `0` to node $n - 1$ and return them in **any order**, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches.

## Complexity detail
- **Time Complexity**: $O(V + E + P \cdot V)$ — Operation count bound.
- **Space Complexity**: $O(V + E + P \cdot V)$ — Auxiliary memory allocation bound.
