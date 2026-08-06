## Description

You are given a tree with `n` nodes numbered from `0` to `n - 1` in the form of a parent array `parent` where `parent[i]` is the parent of `i^th` node. The root of the tree is node `0`. Find the `k^th` ancestor of a given node.

The `k^th` ancestor of a tree node is the `k^th` node in the path from that node to the root node.

Implement the `TreeAncestor` class:

<ul>
	<li>`TreeAncestor(int n, int[] parent)` Initializes the object with the number of nodes in the tree and the parent array.</li>
	<li>`int getKthAncestor(int node, int k)` return the `k^th` ancestor of the given node `node`. If there is no such ancestor, return `-1`.</li>
</ul>
