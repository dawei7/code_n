[TOC]

## Solution

---

### Approach 1: Depth First Search (DFS)


**Intuition**

<center><img src="images/297_BST.png" width="550px" /></center>

The **serialization** of a `Binary Search Tree` is essentially to encode its values and more importantly its structure. One can traverse the tree to accomplish the above task. And it is well known that we have two general strategies to do so:

- *Breadth First Search* (`BFS`)

    We scan through the tree level by level, following the order of height, from top to bottom. The nodes on higher levels would be visited before the ones with lower levels.
     
- *Depth First Search* (`DFS`)

    In this strategy, we adopt `depth` as the priority, so that one would start from a root and reach all the way down to a certain leaf, and then back to the root to reach another branch.

    The DFS strategy can further be distinguished as `preorder`, `inorder`, and `postorder` depending on the relative order among the root node, left node, and right node.
    
In this task, however, the `DFS` strategy is more adapted to our needs, since the linkage among the adjacent nodes is naturally encoded in the order, which is rather helpful for the later task of **deserialization**. 

Therefore, in this solution, we demonstrate an example with the `preorder` DFS strategy. One can check out more tutorials about `Binary Search Tree` on the [LeetCode Explore](https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/).

**Algorithm**

First of all, here is the definition of the ```TreeNode``` which we will use in the following implementation.


```python
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```




The preorder DFS traverse follows *recursively* the order of `root -> left subtree -> right subtree`.

As an example, let's serialize the following tree. Note that serialization contains information about the node values as well as the information about the tree structure.


<!--![LIS](images/297_tr.gif)-->


![Slide 1](images/slideshow_297_LIS_297_sl_1.png)

![Slide 2](images/slideshow_297_LIS_297_sl_2.png)

![Slide 3](images/slideshow_297_LIS_297_sl_3.png)

![Slide 4](images/slideshow_297_LIS_297_sl_4.png)

![Slide 5](images/slideshow_297_LIS_297_sl_5.png)

![Slide 6](images/slideshow_297_LIS_297_sl_6.png)

![Slide 7](images/slideshow_297_LIS_297_sl_7.png)

![Slide 8](images/slideshow_297_LIS_297_sl_8.png)

![Slide 9](images/slideshow_297_LIS_297_sl_9.png)

![Slide 10](images/slideshow_297_LIS_297_sl_10.png)

![Slide 11](images/slideshow_297_LIS_297_sl_11.png)

![Slide 12](images/slideshow_297_LIS_297_sl_12.png)




We start from the root, node `1`, the serialization string is ```1,```. Then we jump to its left subtree with the root node `2`, and the serialization string becomes ```1,2,```. Now starting from node `2`, we visit its left node `3` (```1, 2, 3, None, None,```) and right node `4` (```1, 2, 3, None, None, 4, None, None```) sequentially. Note that ```None, None,``` appears for each leaf to mark the absence of left and right child nodes, this is how we save the tree structure during the serialization. And finally, we get back to the root node `1` and visit its right subtree which happens to be a leaf node `5`. Finally, the serialization string is done as ```1, 2, 3, None, None, 4, None, None, 5, None, None,```.



```python
# Serialization 
class Codec:

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')
```


Now let's deserialize the serialization string constructed above ```1,2,3,None,None,4,None,None,5,None,None,```. It goes along the string, initiates the node value and then calls itself to construct its left and right child nodes. 


```python
# Deserialization 
class Codec:

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
```


**Complexity Analysis**

* Time complexity: in both serialization and deserialization functions, we visit each node exactly once, thus the time complexity is $$O(N)$$, where $$N$$ is the number of nodes, *i.e.* the size of the tree. 

* Space complexity: in both serialization and deserialization functions, we keep the entire tree, either at the beginning or at the end, therefore, the space complexity is $$O(N)$$. 
 
The solutions with BFS or other DFS strategies normally will have the same time and space complexity.
 
**Further Space Optimization**

In the above solution, we store the node value and the references to ```None``` child nodes, which means $$N \cdot V + 2N$$ complexity, where $$V$$ is the size of the value. That is called *natural serialization* and has been implemented above.

The $$N \cdot V$$ component here is the encoding of values, and can't be optimized further, but there is a way to reduce the $$2N$$ part which is the encoding of the tree structure.

The number of unique binary tree structures that can be constructed using `n` nodes is $$C(n)$$, where $$C(n)$$ is the `nth` Catalan number. Please refer to [this article](https://leetcode.com/articles/unique-binary-search-trees/) for more information.

There are $$C(n)$$ possible structural configurations of a binary tree with n nodes, so the largest index value that we might need to store is $$C(n) - 1$$. That means storing the index value could require up to 1 bit for $$n \leq 2$$, or $$\lceil log_2(C(n) - 1) \rceil$$ bits for $$n > 2$$.

In this way, one could reduce the encoding of the tree structure by $$\log N$$. More precisely, the [Catalan numbers](https://en.wikipedia.org/wiki/Catalan_number) grow as $$C(n) \sim \frac{4^n}{n^{3/2}\sqrt{\pi}}$$ and hence the theoretical minimum of storage for the tree structure that could be achieved is $$log(C(n)) \sim 2n - \frac{3}{2}\log(n) - \frac{1}{2}\log(\pi)$$