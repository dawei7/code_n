## General
Given the `root` of a binary tree, the depth of each node is **the shortest distance to the root**, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(h)$ — Auxiliary memory allocation bound.
