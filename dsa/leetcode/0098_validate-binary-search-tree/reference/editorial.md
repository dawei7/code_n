[TOC]

## Video Solution

---

<div>
    <div class="video-container">
        <iframe src="https://player.vimeo.com/video/490012303" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>
</div>

<div>
</div>

## Solution Article

---

### Tree definition

First of all, here is the definition of the ```TreeNode``` which we would use.

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None
```

---
#### Intuition

On the first sight, the problem is trivial. Let's traverse the tree and check at each step if `node.right.val > node.val` and `node.left.val < node.val`. This approach would even work for some trees

![compute](images/98_not_bst.png)

The problem is this approach will not work for all cases. Not only the right child should be larger than the node but all the elements in the right subtree. Here is an example :

![compute](images/98_not_bst_3.png)

That means one should keep both upper and lower limits for each node while traversing the tree, and compare the node value not with children values but with these limits.

---
### Approach 1: Recursive Traversal with Valid Range

The idea above could be implemented as a recursion. One compares the node value with its upper and lower limits if they are available. Then one repeats the same step recursively for left and right subtrees.

![Slide 1](images/slideshow_98_LIS_98_slide_1.png)

![Slide 2](images/slideshow_98_LIS_98_slide_2.png)

![Slide 3](images/slideshow_98_LIS_98_slide_3.png)

![Slide 4](images/slideshow_98_LIS_98_slide_4.png)

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True

            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return validate(node.right, node.val, high) and validate(
                node.left, low, node.val
            )

        return validate(root)
```

**Complexity Analysis**

* Time complexity: $\mathcal{O}(N)$ since we visit each node exactly once.
* Space complexity: $\mathcal{O}(N)$ since we keep up to the entire tree.

---

### Approach 2: Iterative Traversal with Valid Range

The above recursion could be converted into iteration, with the help of an explicit stack. DFS would be better than BFS since it works faster here.

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
```

**Complexity Analysis**

* Time complexity: $\mathcal{O}(N)$ since we visit each node exactly once.
* Space complexity: $\mathcal{O}(N)$ since we keep up to the entire tree.

---

### Approach 3: Recursive Inorder Traversal

**Algorithm**

Let's use the order of nodes in the [inorder traversal](https://leetcode.com/articles/binary-tree-inorder-traversal/)

`Left -> Node -> Right`.

![postorder](images/145_transverse.png)

Here the nodes are enumerated in the order you visit them, and you could follow `1-2-3-4-5` to compare different strategies.

`Left -> Node -> Right` order of inorder traversal means for BST that each element should be smaller than the next one.

Hence the algorithm with $\mathcal{O}(N)$ time complexity and $\mathcal{O}(N)$ space complexity could be simple:

- Compute inorder traversal list `inorder`.

- Check if each element in `inorder` is smaller than the next one.

![postorder](images/98_bst_inorder.png)

> Do we need to keep the whole `inorder` traversal list?

Actually, no. The last added inorder element is enough to ensure at each step that the tree is BST (or not). Hence one could merge both steps into one and reduce the used space.

**Code**

We can implement the algorithm recursively.

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)
```

**Complexity Analysis**

* Time complexity: $\mathcal{O}(N)$ in the worst case when the tree is a BST or the "bad" element is a rightmost leaf.

* Space complexity: $\mathcal{O}(N)$ for the space on the run-time stack.

---

### Approach 4: Iterative Inorder Traversal

Alternatively, we could implement the above algorithm iteratively.

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
```

**Complexity Analysis**

* Time complexity: $\mathcal{O}(N)$ in the worst case when the tree is BST or the "bad" element is the rightmost leaf.

* Space complexity: $\mathcal{O}(N)$ to keep `stack`.