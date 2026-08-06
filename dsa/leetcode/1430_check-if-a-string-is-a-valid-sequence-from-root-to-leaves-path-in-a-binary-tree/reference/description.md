## Description

Each path that starts at the root of a binary tree and ends at a leaf defines a **valid sequence**: read the node values in order while moving from each parent to one of its children.

The target string is represented by an integer array `arr`; concatenating its entries gives the sequence to check. A matching prefix is not enough. The first array value must match the root, consecutive values must follow connected parent-child steps, and the final value must be read at a leaf.

Determine whether `arr` is exactly one of the tree's valid root-to-leaf sequences.
