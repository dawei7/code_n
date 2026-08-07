## Description

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">root = [1,null,2,3]</span>

**Output:** <span class="example-io">[1,3,2]</span>

**Explanation:**

![](images/screenshot-2024-08-29-202743.png)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">root = [1,2,3,4,5,null,8,null,null,6,7,9]</span>

**Output:** <span class="example-io">[4,2,6,5,7,1,3,9,8]</span>

**Explanation:**

![](images/tree_2.png)

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">root = []</span>

**Output:** <span class="example-io">[]</span>

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">root = [1]</span>

**Output:** <span class="example-io">[1]</span>

</div>

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 100]`.

	- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?
