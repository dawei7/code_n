## General
Given the `root` of a binary tree, each node in the tree has a distinct value, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, binary tree node references (`val`, `left`, `right`) to traverse structural hierarchies. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N+D)$ — Operation count bound.
- **Space Complexity**: $O(N+D)$ — Auxiliary memory allocation bound.
