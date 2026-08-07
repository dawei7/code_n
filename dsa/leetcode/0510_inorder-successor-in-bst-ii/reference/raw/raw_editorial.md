[TOC]

## Solution

--- 

### Successor and Predecessor

> Successor = "after node", i.e. the next node in the inorder traversal, or the smallest node _after_ the current one.  

> Predecessor = "before node", i.e. the previous node in the inorder traversal, or the largest node _before_ the current one.  

![img](images/succ.png)
<br />
<br />


---
### Approach 1: Iteration

**Intuition**

There are two possible situations here :

- Node has a right child, and hence its successor is somewhere lower in the tree. To find the successor, go to the right once and then as many times to the left as you could.

![pic](images/right_child2.png)

- Node has no right child, then its successor is somewhere upper in the tree. To find the successor, go up to the node that is _left_ child of its parent. The answer is the parent. Beware that there could be no successor (= null successor) in such a situation.

![pac](images/case.png)

---

![fic](images/casenull.png)


**Algorithm**

1. If the node has a right child, and its successor is somewhere lower in the tree. Go to the right once and then as many times to the left as you can. Return the node you end up with.

2. Node has no right child, and hence its successor is somewhere upper in the tree. Go up till the node that is _left_ child of its parent. The answer is the parent.

**Implementation**


```python
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # the successor is somewhere lower in the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # the successor is somewhere upper in the tree
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(H)$$, where $$H$$ is the height of the tree. That means $$\mathcal{O}(\log N)$$ in the average case, and $$\mathcal{O}(N)$$ in the worst case, where $$N$$ is the number of nodes in the tree.
* Space complexity: $$\mathcal{O}(1)$$, since no additional space is allocated during the calculation.