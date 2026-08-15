### 1. Description

Given the `root` of a binary search tree and an integer `k`, return `true` *if there exist two elements in the BST such that their sum is equal to* `k`, *or* `false` *otherwise*.

### 2. Function Contract

**Methods**

- `TreeNode(val=0, left=None, right=None)`: Initializes the data structure.
- `findTarget(root: Optional[TreeNode], k: int) -> `bool``: Executes operation.

### 3. Examples

#### Example 1

![](images/sum_tree_1.jpg)

- **Input:** `root = [5,3,6,2,4,null,7], k = 9`
- **Output:** `true`

#### Example 2

![](images/sum_tree_2.jpg)

- **Input:** `root = [5,3,6,2,4,null,7], k = 28`
- **Output:** `false`

### 4. Constraints

- The number of nodes in the tree is in the range $[1, 10^{4}]$.

- $-10^{4} \le \text{Node.val} \le 10^{4}$

- `root` is guaranteed to be a **valid** binary search tree.

- $-10^{5} \le k \le 10^{5}$
