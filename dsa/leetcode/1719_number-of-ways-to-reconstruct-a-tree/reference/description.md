## Description

You are given an array `pairs`, where `pairs[i] = [x_i, y_i]`, and:

<ul>
	<li>There are no duplicates.</li>
	<li>`x_i < y_i`</li>
</ul>

Let `ways` be the number of rooted trees that satisfy the following conditions:

<ul>
	<li>The tree consists of nodes whose values appeared in `pairs`.</li>
	<li>A pair `[x_i, y_i]` exists in `pairs` **if and only if** `x_i` is an ancestor of `y_i` or `y_i` is an ancestor of `x_i`.</li>
	<li>**Note:** the tree does not have to be a binary tree.</li>
</ul>

Two ways are considered to be different if there is at least one node that has different parents in both ways.

Return:

<ul>
	<li>`0` if `ways == 0`</li>
	<li>`1` if `ways == 1`</li>
	<li>`2` if `ways > 1`</li>
</ul>

A **rooted tree** is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

An **ancestor** of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.
