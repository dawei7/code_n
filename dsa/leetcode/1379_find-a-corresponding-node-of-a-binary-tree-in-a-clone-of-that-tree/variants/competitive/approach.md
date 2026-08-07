## General
Given two binary trees `original` and `cloned` and given a reference to a node `target` in the original tree, the algorithm executes a single-pass linear scan through input elements. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(N)$ — Auxiliary memory allocation bound.
