## Description

You are given the `root` of a complete binary tree. Every level above the last is full, and any nodes on the last level occupy the leftmost positions.

For a node `x`, consider the subtree rooted at `x`: it contains `x` itself and every descendant below it. The node is **dominant** when its own value equals the maximum value anywhere in that subtree. Another node may share the same maximum value; equality still makes `x` dominant.

Return the total number of dominant nodes in the tree.
