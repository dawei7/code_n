
## Solution
---
### Approach 1: Depth-First Search

**Intuition and Algorithm**

Let's output all the values of the array.  After, we can check that they are all equal.

To output all the values of the array, we perform a depth-first search.

```python
class Solution(object):
    def isUnivalTree(self, root):
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity:  $O(N)$.
<br />
<br />

---
### Approach 2: Recursion

**Intuition and Algorithm**

A tree is univalued if both its children are univalued, plus the root node has the same value as the child nodes.

We can write our function recursively.  $\text{left}_{correct}$ will represent that the left child is correct: ie., that it is univalued, and the root value is equal to the left child's value.  $\text{right}_{correct}$ will represent the same thing for the right child.  We need both of these properties to be true.

```python
class Solution(object):
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the number of nodes in the given tree.

* Space Complexity:  $O(H)$, where $H$ is the height of the given tree.
<br />
<br />