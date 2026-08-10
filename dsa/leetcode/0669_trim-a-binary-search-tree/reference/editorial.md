## Solution Article

---
### Approach #1: Recursion

**Intuition**

Let `trim(node)` be the desired answer for the subtree at that node. We can construct the answer recursively.

**Algorithm**

When $\text{node.val > high}$, we know that the trimmed binary tree must occur to the left of the node. Similarly, when $\text{node.val < low}$, the trimmed binary tree occurs to the right of the node. Otherwise, we will trim both sides of the tree.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the total number of nodes in the given tree. We visit each node at most once.

* Space Complexity: $O(N)$. Even though we don't explicitly use any additional memory, the call stack of our recursion could be as large as the number of nodes in the worst case.

---