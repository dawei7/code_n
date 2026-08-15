### 1. Description

Given the `root` of a binary tree, return *the same tree where every subtree (of the given tree) not containing a *`1`* has been removed*.

A subtree of a node `node` is `node` plus every node that is a descendant of `node`.

### 2. Function Contract

**Methods**

- `TreeNode(val=0, left=None, right=None)`: Initializes the data structure.
- `pruneTree(root: Optional[TreeNode]) -> `Optional[TreeNode]``: Executes operation.

### 3. Examples

#### Example 1

![](images/1028_2.png)

- **Input:** `root = [1,null,0,0,1]`
- **Output:** `[1,null,0,null,1]`
- **Explanation:** Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

#### Example 2

![](images/1028_1.png)

- **Input:** `root = [1,0,1,0,0,0,1]`
- **Output:** `[1,null,1,null,1]`

#### Example 3

![](images/1028.png)

- **Input:** `root = [1,1,0,1,1,0,1,0]`
- **Output:** `[1,1,0,1,1,null,1]`

### 4. Constraints

- The number of nodes in the tree is in the range `[1, 200]`.

- `Node.val` is either `0` or `1`.
