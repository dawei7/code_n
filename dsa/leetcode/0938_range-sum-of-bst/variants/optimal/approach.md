## General
Given the `root` node of a binary search tree and two integers `low` and `high`, return *the sum of values of all nodes with a value in the **inclusive** range *`[low, high]`, the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(h+v)$ — Operation count bound.
- **Space Complexity**: $O(h)$ — Auxiliary memory allocation bound.
