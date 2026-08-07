## Description

You are given the `root` of a <span data-keyword="complete-binary-tree">complete binary tree</span>.

A node `x` is called **dominant** if its value is equal to the maximum value among all nodes in the <span data-keyword="subtree">subtree</span> rooted at `x`.

Return the number of dominant nodes in the tree.

**Example 1:**

<div class="example-block">

![](images/tnew.png)

**Input:** <span class="example-io">root = [5,3,8,2,4,7,1]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- The leaf nodes with values 2, 4, 7, and 1 are dominant.

	- The node with value 8 is dominant because its value is the maximum value in its subtree `[8, 7, 1]`.

	- Thus, the answer is 5.

</div>

**Example 2:**

<div class="example-block">

![](images/t9.png)

**Input:** <span class="example-io">root = [1,2,3,1,2]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- The leaf nodes with values 1, 2, and 3 are dominant.

	- The node with value 2 whose subtree is `[2, 1, 2]` is dominant because its value is the maximum value in its subtree.

	- Thus, the answer is 4.

</div>

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^5]`.

	- `1 <= Node.val <= 10^9`

	- The tree is guaranteed to be a complete binary tree.
