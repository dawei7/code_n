### 1. Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

### 2. Function Contract

**Inputs**

- `root`: The `TreeNode` root of a binary tree with unique values.
- `p`: The first target `TreeNode` in that tree.
- `q`: The second target `TreeNode` in that tree.

JSON cases encode `root` in level order and identify `p` and `q` by their unique values. The runner resolves both targets to nodes in the reconstructed tree before calling `solve(root, p, q)`.

**Return value**

Return the lowest common ancestor `TreeNode`. The runner displays and validates its value.

### 3. Examples

#### Example 1

![](images/binarytree.png)

- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
- **Output:** `3`
- **Explanation:** The LCA of nodes 5 and 1 is 3.

#### Example 2

![](images/binarytree.png)

- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
- **Output:** `5`
- **Explanation:** The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

#### Example 3

- **Input:** `root = [1,2], p = 1, q = 2`
- **Output:** `1`

### 4. Constraints

- The number of nodes in the tree is in the range $[2, 10^{5}]$.

- $-10^{9} \le \text{Node.val} \le 10^{9}$

- All `Node.val` are **unique**.

- $p \neq q$

- `p` and `q` will exist in the tree.
