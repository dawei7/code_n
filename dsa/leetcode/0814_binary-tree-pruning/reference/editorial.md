
---
### Approach #1: Recursion [Accepted]

**Intuition**

Prune children of the tree recursively.  The only decisions at each node are whether to prune the left child or the right child.

**Algorithm**

We'll use a function `containsOne(node)` that tells us whether the subtree at this `node` contains a `1`, and prunes all subtrees that do not contain `1`.

If for example, `node.left` subtree does not contain a one, then we should prune it via $\text{node.left} = null$.

Also, the parent needs to be checked.  If for example the tree is a single node `0`, the answer is an empty tree.

```python
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def contains_one(node: TreeNode) -> bool:
            if not node:
                return False

            # Check if any node in the left subtree contains a 1.
            left_contains_one = contains_one(node.left)

            # Check if any node in the right subtree contains a 1.
            right_contains_one = contains_one(node.right)

            # If the left subtree does not contain a 1, prune the subtree.
            if not left_contains_one:
                node.left = None

            # If the right subtree does not contain a 1, prune the subtree.
            if not right_contains_one:
                node.right = None

            # Return True if the current node or its left or right subtree contains a 1.
            return node.val or left_contains_one or right_contains_one

        # Return the pruned tree if the tree contains a 1, otherwise return None.
        return root if contains_one(root) else None
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the number of nodes in the tree.  We process each node once.

* Space Complexity: $O(N)$, the recursion call stack can be as large as the height $H$ of the tree. In the worst case scenario, $H=N$, when the tree is skewed.