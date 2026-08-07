[TOC]

## Solution

---

### Prerequisites

To solve this problem we will use recursive and iterative inorder traversals. Here are prerequisites you might want to check:

1. There are three DFS ways to traverse the tree: preorder, postorder, and inorder. Please check two minutes picture explanation, if you don't remember them quite well: [here is the Python version](https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line) and [here is Java version](https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/328601/all-dfs-traversals-preorder-postorder-inorder-in-java-in-5-lines).

2. > Inorder traversal of BST is an array sorted in ascending order.

3. To compute in inorder traversal follow the direction `Left -> Node -> Right`.


```python
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
```


![traversal](images/inorder.png)
<br />
<br />


---
### Approach 1: Recursive Inorder Traversal + Sort, Linearithmic Time.

Let's start with the shortest possible solution: 

- Implement recursive inorder traversal, 1 line in Python, 5 lines in Java.

- Compute inorder traversal of each tree.

- Merge both lists and then sort the result.

![traversal](images/recursive_inorder.png)

This solution takes one minute to write, but the time complexity is linearithmic. 

**Implementation**


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        return sorted(inorder(root1) + inorder(root2))
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}((N + M)\log(M + N))$$, where $$M$$ and $$N$$ are node numbers. To build inorder traversals takes $$\mathcal{O}(N + M)$$, to merge and sort the resulting lists - $$\mathcal{O}((N + M)\log(M + N))$$.
    
* Space complexity: $$\mathcal{O}(N + M)$$ to keep the output. 
<br />
<br />


---
### Approach 2: Iterative Inorder Traversal, One Pass, Linear Time.

**Intuition**

Now let's optimize the first approach. 

First, since both inorder traversals are already sorted, [one could merge them into one sorted list in linear time](https://leetcode.com/articles/merged-two-sorted-lists/). However, it's still a two-pass solution: first to build two inorder traversals and then to merge them.

A more elegant way here is to build iteratively inorder traversals for both trees in parallel, and at each step update the output list by the smallest value between both trees. That will be a pass solution. Here is how it works:

![traversal](images/iterative.png)

**Algorithm**

- Do iterative inorder traversal of both trees in parallel.

    - At each step add the smallest available value in the output.
     
- Return output list.

**Implementation**



![Slide 1](images/slideshow_1305_LIS_1305_slide_1.png)

![Slide 2](images/slideshow_1305_LIS_1305_slide_2.png)

![Slide 3](images/slideshow_1305_LIS_1305_slide_3.png)

![Slide 4](images/slideshow_1305_LIS_1305_slide_4.png)

![Slide 5](images/slideshow_1305_LIS_1305_slide_5.png)

![Slide 6](images/slideshow_1305_LIS_1305_slide_6.png)

![Slide 7](images/slideshow_1305_LIS_1305_slide_7.png)

![Slide 8](images/slideshow_1305_LIS_1305_slide_8.png)

![Slide 9](images/slideshow_1305_LIS_1305_slide_9.png)

![Slide 10](images/slideshow_1305_LIS_1305_slide_10.png)




```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, output = [], [], []
        
        while root1 or root2 or stack1 or stack2:
            # update both stacks
            # by going left till possible
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            # Add the smallest value into output,
            # pop it from the stack,
            # and then do one step right
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                output.append(root2.val)   
                root2 = root2.right

        return output
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N + M)$$, where $$M$$ and $$N$$ are node numbers. It's a one-pass approach along each tree. 
    
* Space complexity: $$\mathcal{O}(N + M)$$ to keep the output and both stacks. 
<br />
<br />


---
### Further Reading 

Here we implemented _recursive_ and _iterative_ inorder traversals. There is also _Morris_ inorder traversal, which is used for problems which require constant space solution. Here is a detailed comparison and implementation of all three inorder traversals: [Recover BST](https://leetcode.com/articles/recover-binary-search-tree/). 
<br />
<br />