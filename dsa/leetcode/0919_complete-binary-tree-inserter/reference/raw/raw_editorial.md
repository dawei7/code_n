[TOC]

## Solution
---
### Approach 1: Deque

**Intuition**

Consider all the nodes numbered first by level and then left to right.  Call this the "number order" of the nodes.

At each insertion step, we want to insert into the node with the lowest number (that still has 0 or 1 children).

By maintaining a `deque` (double ended queue) of these nodes in number order, we can solve the problem.  After inserting a node, that node now has the highest number and no children, so it goes at the end of the deque.  To get the node with the lowest number, we pop from the beginning of the deque.

**Algorithm**

First, perform a breadth-first search to populate the `deque` with nodes that have 0 or 1 children, in number order.

Now when inserting a node, the parent is the first element of `deque`, and we add this new node to our `deque`.


```python
class CBTInserter(object):
    def __init__(self, root):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        return self.root
```


**Complexity Analysis**

* Time Complexity:  The preprocessing is $$O(N)$$, where $$N$$ is the number of nodes in the tree.  Each insertion operation thereafter is $$O(1)$$.

* Space Complexity:  $$O(N_{\text{cur}})$$ space complexity, when the size of the tree during the current insertion operation is $$N_{\text{cur}}$$.
<br />
<br />