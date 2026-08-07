[TOC]

## Solution
---
### Approach 1: Depth-First Search

**Intuition**

As we do a pre-order traversal, we will flip nodes on the fly to try to match our voyage with the given one.

If we are expecting the next integer in our voyage to be `voyage[i]`, then there is only at most one choice for path to take, as all nodes have different values.

**Algorithm**

Do a depth first search.  If at any node, the node's value doesn't match the voyage, the answer is `[-1]`.

Otherwise, we know when to flip: the next number we are expecting in the voyage `voyage[i]` is different from the next child.


```python
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) and
                        node.left and node.left.val != voyage[self.i]):
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped
```


**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given tree.

* Space Complexity:  $$O(N)$$.
<br />
<br />