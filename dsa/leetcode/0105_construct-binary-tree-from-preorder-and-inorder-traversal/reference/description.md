## Description

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.
### Function Contract

**Inputs**

- `preorder`: The tree's node values in preorder traversal order.
- `inorder`: The same tree's node values in inorder traversal order.

**Return value**

Return the root of the binary tree represented by both traversals. App results display the returned tree in level order.

### Examples
#### Example 1

![](images/tree.jpg)

- **Input:** $preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]$
- **Output:** `[3,9,20,null,null,15,7]`
#### Example 2

- **Input:** $preorder = [-1], inorder = [-1]$
- **Output:** `[-1]`
### Constraints

- $1 \le \text{preorder.length} \le 3000$

- $\text{inorder.length} = \text{preorder.length}$

- $-3000 \le \text{preorder}[i], \text{inorder}[i] \le 3000$

- `preorder` and `inorder` consist of **unique** values.

- Each value of `inorder` also appears in `preorder`.

- `preorder` is **guaranteed** to be the preorder traversal of the tree.

- `inorder` is **guaranteed** to be the inorder traversal of the tree.