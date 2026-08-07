[TOC]

## Solution

--- 

### Binary Search Tree.

Binary Search Tree is a binary tree where the key in each node 

- is greater than any key stored in the left sub-tree, 

- and less than any key stored in the right sub-tree.

Here is an example:

![bla](images/bst.png)

Such data structure provides the following operations in a logarithmic time: 

- Search. 

- [Insert](https://leetcode.com/articles/insert-into-a-bst/). 

- [Delete](https://leetcode.com/articles/delete-node-in-a-bst/).
<br />
<br />


---
### Approach 1: Recursion

**Algorithm**

The recursion implementation is very straightforward:

- If the tree is empty `root == null` or the value to find is here `val == root.val` - return root.

- If `val < root.val` - go to search into the left subtree `searchBST(root.left, val)`.

- If `val > root.val` - go to search into the right subtree `searchBST(root.right, val)`.

- Return `root`.

![bla](images/recursion.png)

**Implementation**


```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        
        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)
```


**Complexity Analysis**

* Time complexity : $$\mathcal{O}(H)$$, where $$H$$ is a tree height. That results in $$\mathcal{O}(\log N)$$ in the average case, and $$\mathcal{O}(N)$$ in the worst case. 

    Let's compute time complexity with the help of [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) $$T(N) = aT\left(\frac{N}{b}\right) + \Theta(N^d)$$. The equation represents dividing the problem up into $$a$$ subproblems of size $$\frac{N}{b}$$ in $$\Theta(N^d)$$ time. Here at step, there is only one subproblem `a = 1`, its size is half of the initial problem `b = 2`, and all this happens in a constant time `d = 0`, as for the binary search. That means that $$\log_b{a} = d$$ and hence we're dealing with [case 2](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)#Case_2_example) that results in $$\mathcal{O}(n^{\log_b{a}} \log^{d + 1} N)$$ = $$\mathcal{O}(\log N)$$ time complexity.
    
* Space complexity : $$\mathcal{O}(H)$$ to keep the recursion stack, i.e. $$\mathcal{O}(\log N)$$ in the average case, and $$\mathcal{O}(N)$$ in the worst case.
<br />
<br />


---
### Approach 2: Iteration

To reduce the space complexity, one could convert the recursive approach into an iterative one:

- While the tree is not empty `root != null` and the value to find is _not_ here `val != root.val`:

    - If `val < root.val` - go to search into the left subtree `root = root.left`.
    
    - If `val > root.val` - go to search into the right subtree `root = root.right`.

- Return `root`. 

![bla](images/iteration.png)

**Implementation**


```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root
```


**Complexity Analysis**

* Time complexity : $$\mathcal{O}(H)$$, where $$H$$ is a tree height. That results in $$\mathcal{O}(\log N)$$ in the average case, and $$\mathcal{O}(N)$$ in the worst case. 

    Let's compute time complexity with the help of [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) $$T(N) = aT\left(\frac{N}{b}\right) + \Theta(N^d)$$. The equation represents dividing the problem up into $$a$$ subproblems of size $$\frac{N}{b}$$ in $$\Theta(N^d)$$ time. Here at step, there is only one subproblem `a = 1`, its size is half of the initial problem `b = 2`, and all this happens in a constant time `d = 0`, as for the binary search. That means that $$\log_b{a} = d$$ and hence we're dealing with [case 2](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)#Case_2_example) that results in $$\mathcal{O}(n^{\log_b{a}} \log^{d + 1} N)$$ = $$\mathcal{O}(\log N)$$ time complexity.
    
* Space complexity : $$\mathcal{O}(1)$$ since it's a constant space solution.