## General
Given the `root` of a binary tree, return *all root-to-leaf paths in **any order***, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n + output)$ — Operation count bound.
- **Space Complexity**: $O(h)$ — Auxiliary memory allocation bound.
