### 1. Description

Given two nodes of a binary tree `p` and `q`, return *their lowest common ancestor (LCA)*.

Each node will have a reference to its parent node. The definition for `Node` is below:

```
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```

According to the **<a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>**: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow **a node to be a descendant of itself**)."

### 2. Function Contract

**Inputs**

- `p`: A node object in a parent-linked binary tree.
- `q`: A different node object in the same parent-linked binary tree.

```python
class Node:

    def __init__(
        self,
        val: int = 0,
        left: Node | None = None,
        right: Node | None = None,
        parent: Node | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
```

**Return value**

Return the `Node` object that is the lowest common ancestor of `p` and `q`.

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
- **Explanation:** The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
#### Example 3

- **Input:** `root = [1,2], p = 1, q = 2`
- **Output:** `1`

### 4. Constraints

- The number of nodes in the tree is in the range $[2, 10^{5}]$.

- $-10^{9} \le \text{Node.val} \le 10^{9}$

- All `Node.val` are **unique**.

- $p \neq q$

- `p` and `q` exist in the tree.