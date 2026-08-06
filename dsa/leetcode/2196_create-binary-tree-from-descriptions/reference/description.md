## Description

You are given a 2D integer array `descriptions` where `descriptions[i] = [parent_i, child_i, isLeft_i]` indicates that `parent_i` is the **parent** of `child_i` in a **binary** tree of **unique** values. Furthermore,

<ul>
	<li>If `isLeft_i == 1`, then `child_i` is the left child of `parent_i`.</li>
	<li>If `isLeft_i == 0`, then `child_i` is the right child of `parent_i`.</li>
</ul>

Construct the binary tree described by `descriptions` and return *its **root***.

The test cases will be generated such that the binary tree is **valid**.
