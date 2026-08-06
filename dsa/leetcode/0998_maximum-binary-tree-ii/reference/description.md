## Description

A **maximum tree** is a tree where every node has a value greater than any other value in its subtree.

You are given the `root` of a maximum binary tree and an integer `val`.

Just as in the <a href="https://leetcode.com/problems/maximum-binary-tree/" target="_blank">previous problem</a>, the given tree was constructed from a list `a` (`root = Construct(a)`) recursively with the following `Construct(a)` routine:

<ul>
	<li>If `a` is empty, return `null`.</li>
	<li>Otherwise, let `a[i]` be the largest element of `a`. Create a `root` node with the value `a[i]`.</li>
	<li>The left child of `root` will be `Construct([a[0], a[1], ..., a[i - 1]])`.</li>
	<li>The right child of `root` will be `Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]])`.</li>
	<li>Return `root`.</li>
</ul>

Note that we were not given `a` directly, only a root node `root = Construct(a)`.

Suppose `b` is a copy of `a` with the value `val` appended to it. It is guaranteed that `b` has unique values.

Return `Construct(b)`.
