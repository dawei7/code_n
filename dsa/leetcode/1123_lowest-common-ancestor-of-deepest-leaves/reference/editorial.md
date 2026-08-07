[TOC]

## Solution

---

### Approach 1: Recursion

#### Intuition

The problem gives a binary tree and requires returning the lowest common ancestor of its deepest leaf node. The depth of the tree's root node is $0$. We note that all nodes with the maximum depth are leaf nodes. For convenience, we refer to the lowest common ancestor of the deepest leaf nodes as the $\textit{lca}$ node.

We use a recursive method to perform a depth-first search, recursively traversing each node in the tree and returning the maximum depth $d$ of the current subtree and the $\textit{lca}$ node. If the current node is null, we return depth $0$ and an null node. In each search, we recursively search the left and right subtrees, and then compare the depths of the left and right subtrees:

- If the left subtree is deeper, the deepest leaf node is in the left subtree, we return \{left subtree depth + $1$, the $\textit{lca}$ node of the left subtree\}
- If the right subtree is deeper, the deepest leaf node is in the right subtree, we return \{right subtree depth + $1$, the $\textit{lca}$ node of the right subtree\}
- If both left and right subtrees have the same depth and both have the deepest leaf nodes, we return \{left subtree depth + $1$, current node\}.

Finally, we return the root node's $\textit{lca}$ node.

#### Implementation

```python
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0, None

            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root

        return dfs(root)[1]
```

#### Complexity Analysis

Let $n$ be the number of tree nodes.

- Time complexity: $O(n)$

    We only need to traverse all the nodes in the tree once.

- Space complexity: $O(n)$

    The space complexity is mainly the recursive space, with the worst case being $O(n)$.

---