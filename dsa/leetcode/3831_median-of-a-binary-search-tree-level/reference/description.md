## Description

You are given the `root` of a **Binary Search Tree (BST)** together with an integer `level`.

The root occupies level $0$. Every other node's level is its distance from the root, measured in edges.

Consider all node values that occur at the requested `level`. Return their **median value**; if that level has no nodes or lies beyond the tree, return `-1`.

To define the median, arrange the level's values in **non-decreasing** order. An odd number of values has one middle element. For an even number, use the **upper median**: the larger of the two middle elements.
