## Description

The **boundary** of a binary tree is formed in this order: the root, the left boundary, every leaf from left to
right, and the right boundary in reverse order.

The left boundary begins with the root's left child. If the root has no left child, this part is empty. From a node
already on that boundary, continue to its left child when one exists; otherwise continue to its right child. The
leftmost leaf is excluded from the left boundary because it belongs to the leaf portion instead.

The right boundary is the mirror image within the root's right subtree. It begins at the right child, prefers right
children, falls back to left children, excludes its final leaf, and is empty when the root has no right child. Its
nodes are placed into the answer from bottom to top.

A leaf has neither a left nor a right child. Under this problem's definition, the root itself is not treated as a
leaf. Given the tree's `root`, return the values of all boundary nodes in the required concatenated order.
