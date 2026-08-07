[TOC]

### Approach #1: Depth-First Search [Accepted]

**Intuition and Algorithm**

After removing some edge from `parent` to `child`, (where the `child` cannot be the original `root`) the subtree rooted at `child` must be half the sum of the entire tree.

Let's record the sum of every subtree. We can do this recursively using a depth-first search. After, we should check that half the sum of the entire tree occurs somewhere in our recording (and not from the total of the entire tree.)

Our careful treatment and analysis above prevented errors in the case of these trees:
```python
  0
 / \
-1  1

 0
  \
   0
```


```python
class Solution(object):
    def checkEqualTree(self, root):
        seen = []

        def sum_(node):
            if not node:
                return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            return seen[-1]

        total = sum_(root)
        seen.pop()
        return total / 2.0 in seen
```


**Complexity Analysis**

* Time Complexity: $$O(N)$$ where $$N$$ is the number of nodes in the input tree. We traverse every node.

* Space Complexity: $$O(N)$$, the size of `seen`, and the implicit call stack in our DFS.