## Description

Every node in a binary tree has `left`, `right`, and `parent` pointers. Given the original `root` and an existing leaf node, restructure the tree so that `leaf` becomes the new root while preserving every node and every subtree not on the leaf-to-root path.

For each path node `cur` other than the old root, move an existing left child to `cur.right`, make `cur`'s former parent its new left child, and clear the former parent's link back to `cur`. The contract guarantees each such `cur` has at most one child when processed. All child and `parent` pointers must agree in the returned tree.
