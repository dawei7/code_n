### 1. Description

Given the `root` of an n-ary tree, return *the preorder traversal of its nodes' values*.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

### 2. Function Contract

**Methods**

- `Node(val: Optional[int] = None, children: Optional[List['Node']] = None)`: Initializes the data structure.
- `preorder(root: 'Node') -> `List[int]``: Executes operation.

### 3. Examples

#### Example 1

![](images/narytreeexample.png)

- **Input:** `root = [1,null,3,2,4,null,5,6]`
- **Output:** `[1,3,5,6,2,4]`

#### Example 2

![](images/sample_4_964.png)

- **Input:** `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`
- **Output:** `[1,2,3,6,7,11,14,4,8,12,5,9,13,10]`

### 4. Constraints

- The number of nodes in the tree is in the range $[0, 10^{4}]$.

- $0 \le \text{Node.val} \le 10^{4}$

- The height of the n-ary tree is less than or equal to `1000`.

**Follow up:** Recursive solution is trivial, could you do it iteratively?
