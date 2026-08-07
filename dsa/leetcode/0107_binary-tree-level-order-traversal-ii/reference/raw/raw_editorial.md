[TOC]

## Solution

---

### How to traverse the tree

There are two general strategies to traverse a tree:
     
- *Depth First Search* (`DFS`)

    In this strategy, we adopt the `depth` as the priority, so that one
    would start from a root and reach all the way down to a certain leaf,
    and then back to root to reach another branch.

    The DFS strategy can further be distinguished as
    `preorder`, `inorder`, and `postorder` depending on the relative order
    among the root node, left node, and right node.
    
- *Breadth First Search* (`BFS`)

    We scan through the tree level by level, following the order of height,
    from top to bottom. The nodes on a higher level would be visited before the ones 
    on lower levels.
    
In the following figure the nodes are enumerated in the order you visit them,
please follow ```1-2-3-4-5``` to compare different strategies.

![postorder](images/ddfs.png)

Here the problem is to implement split-level BFS traversal : `[[4, 5], [2, 3], [1]]`.
That means we could use one of the `Node->Left->Right` techniques: BFS or DFS Preorder.

We already discussed [three different ways](https://leetcode.com/articles/binary-tree-right-side-view/) 
to implement iterative BFS traversal with the queue, and compared 
[iterative BFS vs. iterative DFS](https://leetcode.com/problems/deepest-leaves-sum/solution/).
Let's use this article to discuss the two most simple and fast techniques:

- Recursive DFS.

- Iterative BFS with two queues.

> Note, that both approaches are root-to-bottom traversals, and we're asked to provide 
bottom-up output. To achieve that, the final result should be reversed. 

<br /> 
<br />


---
### Approach 1: Recursion: DFS Preorder Traversal

**Intuition**

The first step is to ensure that the tree is not empty. 
The second step is to implement the recursive function 
`helper(node, level)`, which takes the current node and its level as the arguments.

**Algorithm for the Recursive Function**

Here is its implementation:

- Initialize the output list `levels`. 
The length of this list determines which level is currently updated.
You should compare this level `len(levels)` with a node level `level`, 
to ensure that you add the node on the correct level.
If you're still on the previous level - 
add the new level by adding a new list into `levels`.

- Append the node value to the last level in `levels`.

- Process recursively child nodes if they are not `None`: 
`helper(node.left / node.right, level + 1)`.

**Implementation**



![Slide 1](images/slideshow_107_LIS_107_slide_1.png)

![Slide 2](images/slideshow_107_LIS_107_slide_2.png)

![Slide 3](images/slideshow_107_LIS_107_slide_3.png)

![Slide 4](images/slideshow_107_LIS_107_slide_4.png)

![Slide 5](images/slideshow_107_LIS_107_slide_5.png)

![Slide 6](images/slideshow_107_LIS_107_slide_6.png)

![Slide 7](images/slideshow_107_LIS_107_slide_7.png)

![Slide 8](images/slideshow_107_LIS_107_slide_8.png)

![Slide 9](images/slideshow_107_LIS_107_slide_9.png)

![Slide 10](images/slideshow_107_LIS_107_slide_10.png)

![Slide 11](images/slideshow_107_LIS_107_slide_11.png)

![Slide 12](images/slideshow_107_LIS_107_slide_12.png)

![Slide 13](images/slideshow_107_LIS_107_slide_13.png)

![Slide 14](images/slideshow_107_LIS_107_slide_14.png)

![Slide 15](images/slideshow_107_LIS_107_slide_15.png)

![Slide 16](images/slideshow_107_LIS_107_slide_16.png)




```python
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node: Optional[TreeNode], level: int) -> None:
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels[::-1]
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$ since each node is processed
exactly once.
 
* Space complexity: $$\mathcal{O}(N)$$ to keep the output structure 
which contains $$N$$ node values.
<br />
<br />


---
### Approach 2: Iteration: BFS Traversal

**Algorithm**

The recursion above could be rewritten in the iteration form.

Let's keep each tree level in the _queue_ structure,
which typically orders elements in a FIFO (first-in-first-out) manner.
In Java one could use [`ArrayDeque` implementation of the `Queue` interface](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html).
In Python using [`Queue` structure](https://docs.python.org/3/library/queue.html)
would be an overkill since it's designed for a safe exchange between multiple threads
and hence requires locking which leads to a performance downgrade. 
In Python the queue implementation with a fast atomic `append()`
and `popleft()` is [`deque`](https://docs.python.org/3/library/collections.html#collections.deque).

**Algorithm**

- Initialize two queues: one for the current level, 
and one for the next. Add root into `nextLevel` queue.

- While `nextLevel` queue is not empty:

    - Initialize the current level `currLevel = nextLevel`,
    and empty the next level `nextLevel`. 
    
    - Iterate over the current level queue:

        - Append the node value to the last level in `levels`.
        
        - Add first _left_ and then _right_ child node into `nextLevel`
        queue.
    
- Return reversed `levels`.

**Implementation**


```python
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        next_level = deque([root])

        while root and next_level:
            curr_level = next_level
            next_level = deque()
            levels.append([])

            for node in curr_level:
                # append the current node value
                levels[-1].append(node.val)
                # process child nodes for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        return levels[::-1]
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$ since each node is processed
exactly once.
 
* Space complexity: $$\mathcal{O}(N)$$ to keep the output structure which
contains $$N$$ node values.