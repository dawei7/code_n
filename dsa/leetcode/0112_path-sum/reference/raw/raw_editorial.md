[TOC]

## Solution

---

### Binary tree definition

First of all, here is the definition of the ```TreeNode``` which we would use in the following implementation.


```python
class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```

<br />
<br />


---
### Approach 1: Recursion

The most intuitive way is to use recursion here. One is going through the tree by considering at each step the node itself and its children. If node *is not* a leaf, one calls recursively `hasPathSum` method for its children with a sum decreased by the current node value. If node *is* a leaf, one check if the current sum is zero, *i.e.* if the initial sum was discovered.


```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(
            root.right, sum
        )
```


**Complexity Analysis**

* Time complexity : we visit each node exactly once, thus the time complexity is $$\mathcal{O}(N)$$, where $$N$$ is the number of nodes.
* Space complexity : in the worst case, the tree is completely unbalanced, *e.g.* each node has only one child node, the recursion call would occur $$N$$ times (the height of the tree), therefore the storage to keep the call stack would be $$\mathcal{O}(N)$$. But in the best case (the tree is completely balanced), the height of the tree would be $$\log(N)$$. Therefore, the space complexity in this case would be $$\mathcal{O}(\log(N))$$.
<br />
<br />


---
### Approach 2: Iterations

**Algorithm**

We could also convert the above recursion into iteration, with the help of stack. DFS would be better than BFS here since it works faster except in the worst case. In the worst case the path `root->leaf` with the given sum is the last considered one and in this case, DFS results in the same productivity as BFS. 

>The idea is to visit each node with the DFS strategy while updating the remaining sum to cumulate at each visit.

So we start from a stack that contains the root node and the corresponding remaining sum which is ```sum - root.val```. Then we proceed to the iterations: pop the current node out of the stack and return ```True``` if the remaining sum is `0` and we're on the leaf node. If the remaining sum is not zero or we're not on the leaf yet then we push the child nodes and corresponding remaining sums into the stack.  

<!--![LIS](images/112_tr.gif)-->


![Slide 1](images/slideshow_112_LIS_112_slide_6.png)

![Slide 2](images/slideshow_112_LIS_112_slide_7.png)

![Slide 3](images/slideshow_112_LIS_112_slide_8.png)

![Slide 4](images/slideshow_112_LIS_112_slide_9.png)

![Slide 5](images/slideshow_112_LIS_112_slide_10.png)

![Slide 6](images/slideshow_112_LIS_112_slide_11.png)

![Slide 7](images/slideshow_112_LIS_112_slide_12.png)

![Slide 8](images/slideshow_112_LIS_112_slide_13.png)




```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        de = [
            (root, sum - root.val),
        ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
```


**Complexity Analysis**

* Time complexity: the same as the recursion approach $$\mathcal{O}(N)$$.
* Space complexity: $$\mathcal{O}(N)$$ since in the worst case, when the tree is completely unbalanced, *e.g.* each node has only one child node, we would keep all $$N$$ nodes in the stack. But in the best case (the tree is balanced), the height of the tree would be $$\log(N)$$. Therefore, the space complexity in this case would be $$\mathcal{O}(\log(N))$$.