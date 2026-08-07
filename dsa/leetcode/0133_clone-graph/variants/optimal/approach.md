## General
Given a reference of a node in a **<a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank">connected</a>** undirected graph, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(V + E)$ — Operation count bound.
- **Space Complexity**: $O(V + E)$ — Auxiliary memory allocation bound.
