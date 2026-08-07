## General
Given the `root` of a Binary Search Tree (BST), return *the minimum difference between the values of any two different nodes in the tree*, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns, uses infinity sentinels for safe boundary initialization.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(h)$ — Auxiliary memory allocation bound.
