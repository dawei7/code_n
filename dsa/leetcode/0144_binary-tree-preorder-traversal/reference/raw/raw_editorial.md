[TOC]

## Solution

---

#### How to traverse the tree


There are two general strategies to traverse a tree:

- *Breadth First Search* (`BFS`)

    We scan through the tree level by level, following the order of height, from top to bottom. The nodes on higher levels would be visited before the ones with lower levels.
     
- *Depth First Search* (`DFS`)

    In this strategy, we adopt the `depth` as the priority, so that one would start from a root and reach all the way down to a certain leaf, and then back to the root to reach another branch.

    The DFS strategy can further be distinguished as `preorder`, `inorder`, and `postorder` depending on the relative order among the root node, left node, and right node.
    
In the following figure, the nodes are enumerated in the order you visit them, please follow ```1-2-3-4-5``` to compare different strategies.

![postorder](images/145_transverse.png)

Here the problem is to implement preorder traversal using iterations.
<br />
<br />


---
#### Approach 1: Iterations

**Algorithm**

First of all, here is the definition of the ```TreeNode``` which we would use in the following implementation.


```python
class TreeNode(object):
    """Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```


Let's start from the root and then at each iteration pop the current node out of the stack and push its child nodes. In the implemented strategy we push nodes into the output list following the order ```Top->Bottom``` and ```Left->Right```, which naturally reproduces preorder traversal.


```python
class Solution(object):
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [
            root,
        ], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output
```




**Complexity Analysis**

* Time complexity: we visit each node exactly once, thus the time complexity is $$\mathcal{O}(N)$$, where $$N$$ is the number of nodes, *i.e.* the size of the tree.

* Space complexity: depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is $$\mathcal{O}(N)$$.
<br />
<br />


---
#### Approach 2: Morris traversal

This approach is based on [Morris's article](https://www.sciencedirect.com/science/article/pii/0020019079900681) which is intended to optimize the space complexity. The algorithm does not use additional space for the computation, and the memory is only used to keep the output. If one prints the output directly along the computation, the space complexity would be $$\mathcal{O}(1)$$.

**Algorithm**

Here the idea is to go down from the node to its predecessor, and each predecessor will be visited twice. For this go one step left if possible and then always right till the end. When we visit a leaf (node's predecessor) first time, it has a zero right child, so we update output and establish the pseudo link ```predecessor.right = root``` to mark the fact the predecessor is visited. When we visit the same predecessor the second time, it already points to the current node, thus we remove the pseudo link and move right to the next node.

If the first step left is impossible, update the output and move right to the next node.

<!--![LIS](images/144_gif.gif)-->


![Slide 1](images/slideshow_144_LIS_144_slide_2.png)

![Slide 2](images/slideshow_144_LIS_144_slide_3.png)

![Slide 3](images/slideshow_144_LIS_144_slide_4.png)

![Slide 4](images/slideshow_144_LIS_144_slide_5.png)

![Slide 5](images/slideshow_144_LIS_144_slide_6.png)

![Slide 6](images/slideshow_144_LIS_144_slide_7.png)

![Slide 7](images/slideshow_144_LIS_144_slide_8.png)

![Slide 8](images/slideshow_144_LIS_144_slide_9.png)

![Slide 9](images/slideshow_144_LIS_144_slide_10.png)

![Slide 10](images/slideshow_144_LIS_144_slide_11.png)

![Slide 11](images/slideshow_144_LIS_144_slide_12.png)

![Slide 12](images/slideshow_144_LIS_144_slide_13.png)

![Slide 13](images/slideshow_144_LIS_144_slide_14.png)

![Slide 14](images/slideshow_144_LIS_144_slide_15.png)

![Slide 15](images/slideshow_144_LIS_144_slide_16.png)

![Slide 16](images/slideshow_144_LIS_144_slide_17.png)


 

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right

        return output
```


**Complexity Analysis**

* Time complexity: we visit each predecessor exactly twice descending down from the node, thus the time complexity is $$\mathcal{O}(N)$$, where $$N$$ is the number of nodes, *i.e.* the size of the tree.

* Space complexity: we use no additional memory for the computation itself, but the output list contains $$N$$ elements, and thus space complexity is $$\mathcal{O}(N)$$.