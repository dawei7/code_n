## Description

Given the `root` of a binary search tree (BST) and an integer `target`, divide the original tree into two subtrees. Every node in the first subtree must have a value smaller than or equal to `target`, while every node in the second must have a value greater than `target`. The tree is not required to contain `target`.

Retain the original structure wherever the partition permits. More precisely, if a node `c` was a child of `p` before the split and both nodes belong to the same resulting subtree, then `c` must still have `p` as its parent afterward.

Return the two subtree roots in order: the root for values at most `target` first, followed by the root for values greater than `target`.
