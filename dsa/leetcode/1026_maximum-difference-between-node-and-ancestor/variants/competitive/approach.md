## General
Given the `root` of a binary tree, find the maximum value `v` for which there exist **different** nodes `a` and `b` where $v = |\text{a.val} - \text{b.val}|$ and `a` is an ancestor of `b`, the algorithm executes a single-pass linear scan through input elements. It utilizes binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N)$ — Operation count bound.
- **Space Complexity**: $O(H)$ — Auxiliary memory allocation bound.
