## General
Given the `root` of a binary tree and an integer `targetSum`, return *all **root-to-leaf** paths where the sum of the node values in the path equals *`targetSum`*. Each path should be returned as a list of the node **values..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n + L)$ — Operation count bound.
- **Space Complexity**: $O(h)$ — Auxiliary memory allocation bound.
