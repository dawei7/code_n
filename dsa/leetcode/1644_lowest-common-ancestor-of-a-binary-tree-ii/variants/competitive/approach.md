## General
Given the `root` of a binary tree, return *the lowest common ancestor (LCA) of two given nodes, *`p`* and *`q`. If either node `p` or `q` **does not exist** in the tree, return `null`. All values of the nodes in the tree ar..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(h)$ — Auxiliary memory allocation bound.
