## Description

You are given the `root` of a binary tree with `n` nodes, where each node is uniquely assigned a value from `1` to `n`. You are also given a sequence of `n` values `voyage`, which is the **desired** <a href="https://en.wikipedia.org/wiki/Tree_traversal#Pre-order" target="_blank">**pre-order traversal**</a> of the binary tree.

Any node in the binary tree can be **flipped** by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/15/fliptree.jpg" style="width: 400px; height: 187px;" />
Flip the **smallest** number of nodes so that the **pre-order traversal** of the tree **matches** `voyage`.

Return *a list of the values of all **flipped** nodes. You may return the answer in **any order**. If it is **impossible** to flip the nodes in the tree to make the pre-order traversal match *`voyage`*, return the list *`[-1]`.
