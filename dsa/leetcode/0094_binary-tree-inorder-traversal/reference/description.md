## Description

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.
### Function Contract

**Inputs**

- `root`: The binary tree root, or `null` for an empty tree.

**Return value**

Return all node values in left-subtree, node, right-subtree order.

### Examples
#### Example 1

<div class="example-block">
**Input:** root = [1,null,2,3]

**Output:** [1,3,2]

**Explanation:**

![](images/screenshot-2024-08-29-202743.png)

</div>
#### Example 2

<div class="example-block">
**Input:** root = [1,2,3,4,5,null,8,null,null,6,7,9]

**Output:** [4,2,6,5,7,1,3,9,8]

**Explanation:**

![](images/tree_2.png)

</div>
#### Example 3

<div class="example-block">
**Input:** root = []

**Output:** []

</div>
#### Example 4

<div class="example-block">
**Input:** root = [1]

**Output:** [1]

</div>
### Constraints

- The number of nodes in the tree is in the range `[0, 100]`.

- $-100 \le \text{Node.val} \le 100$

**Follow up:** Recursive solution is trivial, could you do it iteratively?