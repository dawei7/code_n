## Description

Given an array `arr` of positive integers, consider all binary trees such that:

<ul>
	<li>Each node has either `0` or `2` children;</li>
	<li>The values of `arr` correspond to the values of each **leaf** in an in-order traversal of the tree.</li>
	<li>The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.</li>
</ul>

Among all possible binary trees considered, return *the smallest possible sum of the values of each non-leaf node*. It is guaranteed this sum fits into a **32-bit** integer.

A node is a **leaf** if and only if it has zero children.
