[TOC]

## Video Solution
---

<div>
    <div class="video-container">
        <iframe src="https://player.vimeo.com/video/483333214" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>
</div>

<div>&nbsp;
</div>

## Solution Article
---
### Approach 1: Depth First Search

**Intuition and Algorithm**

We traverse the tree using a depth first search.  If `node.val` falls outside the range `[low, high]`, (for example `node.val < low`), then we know that only the right branch could have nodes with value inside `[low, high]`.

We showcase two implementations - one using a recursive algorithm, and one using an iterative one.

**Recursive Implementation**


```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal ans
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        ans = 0
        dfs(root)
        return ans
```


**Iterative Implementation**


```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans
```


**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the tree.

* Space Complexity:  $$O(N)$$

    - For the recursive and iterative implementations, we are performing a **DFS** (Depth-First Search) traversal. The recursive solution requires additional space to maintain the function call stack while the iterative solution requires additional space to maintain the stack.  In both implementations, the worst-case scenario occurs when the tree is of chain shape, and we will reach all the way down to the leaf node. In this case, the space required for the stack is $$O(N)$$. 

---