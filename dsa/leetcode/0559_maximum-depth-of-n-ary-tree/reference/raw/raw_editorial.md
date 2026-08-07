[TOC]

## Solution

**Tree definition**

First of all, please refer to [this article](https://leetcode.com/articles/maximum-depth-of-binary-tree/) for the solution in the case of a binary tree. This article offers the same ideas with a bit of generalization. 

Here is the definition of the ```TreeNode``` which we would use.


```python
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
```

<br />
<br />


---
### Approach 1: Recursion

**Algorithm**

The intuitive approach is to solve the problem by recursion. Here we demonstrate an example with the DFS (Depth First Search) strategy. 


```python
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None: 
            return 0 
        elif root.children == []:
            return 1
        else: 
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1 
```


**Complexity analysis**

* Time complexity: we visit each node exactly once, thus the time complexity is $$\mathcal{O}(N)$$, where $$N$$ is the number of nodes.

* Space complexity: in the worst case, the tree is completely unbalanced, *e.g.* each node has only one child node, the recursion call would occur $$N$$ times (the height of the tree), therefore the storage to keep the call stack would be $$\mathcal{O}(N)$$. But in the best case (the tree is completely balanced), the height of the tree would be $$\log(N)$$. Therefore, the space complexity in this case would be $$\mathcal{O}(\log(N))$$.
<br />
<br />


---
### Approach 2: Iteration

We could also convert the above recursion into iteration, with the help of stack.

>The idea is to visit each node with the DFS strategy while updating the maximum depth at each visit.

So we start from a stack that contains the root node and the corresponding depth which is ```1```. Then we proceed to the iterations: pop the current node out of the stack and push the child nodes. The depth is updated at each step. 


```python
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """ 
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))
                
        return depth
```
  

**Complexity analysis**

* Time complexity: $$\mathcal{O}(N)$$.

* Space complexity: $$\mathcal{O}(N)$$.