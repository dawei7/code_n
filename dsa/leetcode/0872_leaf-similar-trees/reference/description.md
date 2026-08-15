### 1. Description

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence***.*

![](images/tree.png)

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered *leaf-similar* if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.

### 2. Function Contract

**Methods**

- `TreeNode(val=0, left=None, right=None)`: Initializes the data structure.
- `leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> `bool``: Executes operation.

### 3. Examples

#### Example 1

![](images/leaf-similar-1.jpg)

- **Input:** $root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]$
- **Output:** `true`

#### Example 2

![](images/leaf-similar-2.jpg)

- **Input:** $root1 = [1,2,3], root2 = [1,3,2]$
- **Output:** `false`

### 4. Constraints

- The number of nodes in each tree will be in the range `[1, 200]`.

- Both of the given trees will have values in the range `[0, 200]`.
