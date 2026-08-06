## Description

A binary tree contains exactly one invalid node. Instead of a normal right child, that node's `right` pointer incorrectly references another node at the same depth that lies to its right. Remove the invalid node and its entire genuine descendant subtree while preserving the node reached by the erroneous pointer and every other valid part of the tree.

For serialized custom tests, `root.values` describes the tree before corruption. The fixture's `root.corrupt_right` descriptor identifies the source and target by their unique values; the cOde(n) harness installs that invalid pointer while constructing the `TreeNode` graph, before it calls `solve(root)`.
