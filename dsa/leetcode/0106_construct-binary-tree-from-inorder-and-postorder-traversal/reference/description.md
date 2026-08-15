### 1. Description

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return *the binary tree*.

### 2. Function Contract

**Inputs**

- `inorder`: The tree's node values in inorder traversal order.
- `postorder`: The same tree's node values in postorder traversal order.

**Return value**

Return the root of the binary tree represented by both traversals. App results display the returned tree in level order.

### 3. Examples

#### Example 1

![](images/tree.jpg)

- **Input:** $inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]$
- **Output:** `[3,9,20,null,null,15,7]`

#### Example 2

- **Input:** $inorder = [-1], postorder = [-1]$
- **Output:** `[-1]`

### 4. Constraints

- $1 \le \text{inorder.length} \le 3000$

- $\text{postorder.length} = \text{inorder.length}$

- $-3000 \le \text{inorder}[i], \text{postorder}[i] \le 3000$

- `inorder` and `postorder` consist of **unique** values.

- Each value of `postorder` also appears in `inorder`.

- `inorder` is **guaranteed** to be the inorder traversal of the tree.

- `postorder` is **guaranteed** to be the postorder traversal of the tree.
