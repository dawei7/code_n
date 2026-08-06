## Description

You are given `n` **BST (binary search tree) root nodes** for `n` separate BSTs stored in an array `trees` (**0-indexed**). Each BST in `trees` has **at most 3 nodes**, and no two roots have the same value. In one operation, you can:

<ul>
	<li>Select two **distinct** indices `i` and `j` such that the value stored at one of the **leaves **of `trees[i]` is equal to the **root value** of `trees[j]`.</li>
	<li>Replace the leaf node in `trees[i]` with `trees[j]`.</li>
	<li>Remove `trees[j]` from `trees`.</li>
</ul>

Return* the **root** of the resulting BST if it is possible to form a valid BST after performing *`n - 1`* operations, or** *`null` *if it is impossible to create a valid BST*.

A BST (binary search tree) is a binary tree where each node satisfies the following property:

<ul>
	<li>Every node in the node's left subtree has a value **strictly less** than the node's value.</li>
	<li>Every node in the node's right subtree has a value **strictly greater** than the node's value.</li>
</ul>

A leaf is a node that has no children.
